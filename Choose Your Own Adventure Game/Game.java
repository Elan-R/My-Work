import java.awt.FileDialog;
import java.awt.Frame;
import java.io.*;
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.Scanner;

public class Game {

    String premessage_screen = "/[message]\n\nPress enter to continue...";
    String menu_screen = "/[message]\n\nWhat do you do?\n\n/[key]: /[choice]";
    String postmessage_screen = "/[message]\n\nPress enter to continue...";
    Scanner scanner;
    World world;
    HashMap<String, Object> vars;

    public Game(World world) throws IOException {
        this.world = world;
        vars = new HashMap<>();
        scanner = new Scanner(System.in);
        String s;
        if ((s = world.screens.get("premessage")) != null) {
            premessage_screen = s;
        }
        if ((s = world.screens.get("menu")) != null) {
            menu_screen = s;
        }
        if ((s = world.screens.get("postmessage")) != null) {
            postmessage_screen = s;
        }

        while (world.current != null) {
            world.save();
            print_menu(world.current);
        }
        world.current = world.menus.get("start");
        world.save();
    }

    private void print_menu(Menu menu) {
        for (String msg : menu.premessages) {
            System.out.println(premessage_screen.replace("/[message]", msg));
            scanner.nextLine();
        }

        StringBuilder output = new StringBuilder();
        StringBuilder choice_text = new StringBuilder();
        boolean choices = false;
        for (String s : menu_screen.split("\n")) {
            if (s.contains("/[key]")) {
                choices = true;
            }
            if (choices) {
                choice_text.append('\n').append(s);
            } else {
                output.append('\n').append(s);
            }
        }
        output = new StringBuilder(output.toString().replace("/[message]", menu.message));
        for (Entry<String, String> id : menu.choices.entrySet()) {
            output.append(choice_text.toString().replace("/[key]", id.getKey()).replace("/[choice]", id.getValue()));
        }
        System.out.println(output.toString());
        String next_menu = null;
        String choice = "";
        while (next_menu == null) {
            next_menu = menu.pointers.get((choice = scanner.nextLine().strip()));
            if (next_menu == null) {
                System.out.println("That isn't an option!");
            }
        }
        world.current = world.menus.get(menu.pointers.get(choice));
        for (String msg : menu.postmessages) {
            System.out.println(postmessage_screen.replace("/[message]", msg));
            scanner.nextLine();
        }
    }

    public static void main(String[] args) throws IOException, ClassNotFoundException {
        FileDialog d = new FileDialog((Frame) null, "Select a file to play");
        d.setMode(FileDialog.LOAD);
        d.setVisible(true);
        FileInputStream f = new FileInputStream(new File(d.getDirectory() + d.getFile()).getAbsolutePath());
        ObjectInputStream in = new ObjectInputStream(f);
        new Game((World) in.readObject());
        in.close();
        f.close();
        System.exit(0);
    }
}
