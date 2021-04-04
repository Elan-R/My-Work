import java.awt.FileDialog;
import java.awt.Frame;
import java.io.IOException;

public class Compiler {

    private static String get_file(String message) {
        FileDialog d = new FileDialog((Frame) null, message);
        d.setMode(FileDialog.LOAD);
        d.setVisible(true);
        return d.getDirectory() + d.getFile();
    }

    public static void main(String[] args) throws IOException, Parser.SyntaxError, Parser.GameError {
        World w = new Parser(get_file("Select a file to compile"), true).parse();
        w.save(get_file("Select a file to save to"));
        System.exit(0);
    }
}
