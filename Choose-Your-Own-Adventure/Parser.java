import java.io.FileReader;
import java.io.IOException;
import java.io.Serial;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;
import java.io.File;

public class Parser {

    public static class SyntaxError extends Exception {

        @Serial
        private static final long serialVersionUID = 8859903481032219582L;

        public SyntaxError(String message) {
            super(message);
        }
    }

    public static class GameError extends Exception {

        @Serial
        private static final long serialVersionUID = 1923097375101523583L;

        public GameError(String message) {
            super(message);
        }
    }

    private final FileReader file;
    private final boolean verbose;
    private final HashMap<String, String> screens;
    private final HashMap<String, Menu> menus;
    private int line = 1;

    public Parser(String path, boolean verbose) throws IOException {
        file = new FileReader(new File(path).getAbsolutePath());
        this.verbose = verbose;
        screens = new HashMap<>();
        menus = new HashMap<>();
    }

    private char read() throws IOException {
        char chr = check_comment((char) file.read());
        if (chr == '\n') {
            line++;
        }
        return chr;
    }

    private char check_comment(char chr) throws IOException {
        if (chr == '/') {
            if ((chr = (char) file.read()) == '/') {
                while (file.read() != '\n');
                return (char) file.read();
            }
            if (chr == '*') {
                while (!((chr == '*' ? '*' : file.read()) == '*' && (chr = (char) file.read()) == '/'));
                return (char) file.read();
            }
        }
        return chr;
    }

    private char read_string() throws IOException, SyntaxError {
        char chr = check_escape((char) file.read());
        if (chr == '\n') {
            line++;
        }
        return chr;
    }

    private char check_escape(char chr) throws IOException, SyntaxError {
        if (chr == '\\') {
            switch ((char) file.read()) {
                case 'n':
                    return '\n';
                case '\\':
                    return '\\';
                case 't':
                    return '\t';
                case 'r':
                    return '\r';
                case '"':
                    return '"';
                default:
                    file.close();
                    throw new SyntaxError("Invalid escape character on line " + line + ": \\" + chr);
            }
        }
        if (chr == '"') {
            return 65534;
        }
        return chr;
    }

    private void print(String string) {
        if (verbose) {
            System.out.println(string);
        }
    }

    public World parse() throws IOException, SyntaxError, GameError {
        print("Beginning parsing");
        print("Searching for context");
        char chr;
        while ((chr = read()) != '#' && chr != Character.MAX_VALUE);
        if (chr == Character.MAX_VALUE) {
            print("End of file reached");
            return null;
        }
        while (true) {
            switch (find_context()) {
                case "screen" -> compile_screens();
                case "menu" -> compile_menus();
                default -> {
                    print("Finished parsing");
                    Menu start = menus.get("start");
                    if (start == null) {
                        file.close();
                        throw new GameError("A game needs to have a starting menu with the ID \"start\"");
                    }
                    file.close();
                    return new World(screens, menus, start);
                }
            }
        }
    }

    private String find_context() throws IOException {
        char chr;
        StringBuilder context = new StringBuilder();
        while ((chr = read()) != '#' && chr != Character.MAX_VALUE) {
            context.append(chr);
        }
        if (chr != Character.MAX_VALUE) {
            print("Context found");
        }
        return context.toString().strip().toLowerCase();
    }

    private void compile_screens() throws IOException, SyntaxError {
        print("Compiling screens");
        char chr;
        while ((chr = read()) != Character.MAX_VALUE && chr != '#') {
            if (chr == '{') {
                build_screen();
            }
        }
    }

    private void build_screen() throws IOException, SyntaxError {
        print("Building screen");
        StringBuilder id = new StringBuilder();
        StringBuilder format = new StringBuilder();
        char chr;
        while ((chr = read()) != '"' && chr != '}') {
            id.append(chr);
        }
        print("ID: " + id.toString().strip());
        if (chr == '"') {
            while ((chr = read_string()) != 65534) {
                format.append(chr);
            }
            while (read() != '}');
        }
        print("Format: " + format);
        screens.put(id.toString().strip(), format.toString());
        print("Screen created");
    }

    private void compile_menus() throws IOException, SyntaxError {
        print("Compiling menus");
        char chr;
        while ((chr = read()) != Character.MAX_VALUE && chr != '#') {
            if (chr == '{') {
                build_menu();
            }
        }
    }

    private void build_menu() throws IOException, SyntaxError {
        print("Building menu");
        StringBuilder id = new StringBuilder();
        List<String> premessages = new ArrayList<>(0);
        StringBuilder message = new StringBuilder();
        StringBuilder key = new StringBuilder();
        StringBuilder option = new StringBuilder();
        HashMap<String, String> choices = new HashMap<>();
        StringBuilder pointer = new StringBuilder();
        HashMap<String, String> pointers = new HashMap<>();
        char chr;
        print("Finding ID");
        while ((chr = read()) != '"' && chr != '*' && chr != Character.MAX_VALUE) {
            id.append(chr);
        }
        print("ID: " + id.toString().strip());
        if (chr == '"') {
            print("Finding messages");
            do {
                if (chr == '"') {
                    print("Finding message");
                    if (message.length() != 0) {
                        premessages.add(message.toString());
                        message.setLength(0);
                    }
                    while ((chr = read_string()) != 65534) {
                        message.append(chr);
                    }
                    print("Message: " + message);
                }
            } while ((chr = read()) != '*' && chr != '}');
        }
        if (chr == '*') {
            print("Finding choices");
            do {
                print("Finding choice");
                key.setLength(0);
                option.setLength(0);
                pointer.setLength(0);
                while ((chr = read()) != '*') {
                    key.append(chr);
                }
                print("Key: " + key.toString().strip());
                while (read() != '"');
                while ((chr = read_string()) != 65534) {
                    option.append(chr);
                }
                print("Option: " + option);
                while ((chr = read()) != '*' && chr != '}') {
                    pointer.append(chr);
                }
                print("Pointer: " + pointer.toString().strip());
                choices.put(key.toString().strip(), option.toString());
                print("Created choice");
                pointers.put(key.toString().strip(), pointer.toString().strip());
            } while (chr != '}');
        }
        menus.put(id.toString().strip(), new Menu(id.toString().strip(), premessages, message.toString(), choices, pointers));
        print("Created menu");
    }
}
