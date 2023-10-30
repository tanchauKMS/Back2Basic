package DependenyInjection.Country;

public class Japan implements Country{
    @Override
    public void getName() {
        System.out.println("Japan");
    }
    public void getContinent() {
       System.out.println("Asia");
    }
    
}
