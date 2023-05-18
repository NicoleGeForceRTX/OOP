public class OOP_7 {  
    public static void main(String[] args) {
        Human human1 = new Human();       
    }
}

class Human {
    
    private String name;
    private int age;
    
    public Human() {
        System.out.println("Привет из 1го конструктора!");
    }
    
    public Human(String name) {
        System.out.println("Привет из 2го конструктора!");
        this.name = name;
    }
    
     public Human(String name, int age) {
        System.out.println("Привет из 3го конструктора!");
        this.name = name;
        this.age = age;
    }

    public void setName(String name) { this.name = name; }
    
    public void setAge(int age) { this.age = age; }

}