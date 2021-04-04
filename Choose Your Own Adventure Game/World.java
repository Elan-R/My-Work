import java.io.*;
import java.util.HashMap;

public class World implements Serializable {

    @Serial
    private static final long serialVersionUID = -4242968608117470198L;
    HashMap<String, String> screens;
    HashMap<String, Menu> menus;
    Menu current;
    HashMap<String, Object> vars;
    String file = "";

    public World(HashMap<String, String> screens, HashMap<String, Menu> menus, Menu current, HashMap<String, Object> vars) {
        this.screens = screens;
        this.menus = menus;
        this.current = current;
        this.vars = vars;
    }

    public World(HashMap<String, String> screens, HashMap<String, Menu> menus, Menu current) {
        this.screens = screens;
        this.menus = menus;
        this.current = current;
        vars = new HashMap<String, Object>();
    }

    public void save(String path) throws IOException {
        file = path;
        FileOutputStream f = new FileOutputStream(path);
        ObjectOutputStream out = new ObjectOutputStream(f);
        out.writeObject(this);
        out.close();
        f.close();
    }

    public void save() throws IOException {
        if (file != null && !file.isBlank()) {
            save(file);
        }
    }
}
