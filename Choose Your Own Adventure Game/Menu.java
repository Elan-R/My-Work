import java.io.Serial;
import java.io.Serializable;
import java.util.List;
import java.util.HashMap;

public class Menu implements Serializable {

    @Serial
    private static final long serialVersionUID = -5113327787247643595L;
    String id;
    List<String> premessages;
    String message;
    HashMap<String, String> choices;
    HashMap<String, String> pointers;

    public Menu(String id, List<String> premessages, String message, HashMap<String, String> choices, HashMap<String, String> pointers) {
        this.id = id;
        this.premessages = premessages;
        this.message = message;
        this.choices = choices;
        this.pointers = pointers;
    }
}
