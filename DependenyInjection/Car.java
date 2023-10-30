package DependenyInjection;
import DependenyInjection.Country.Country;
import DependenyInjection.Engine.Engine;
import DependenyInjection.Engine.SuzukiEngine;
import DependenyInjection.Engine.YamahaEngine;

public class Car {
    private Country country;
    private Engine engine;

    public Car() {

    }

    public Car(Engine engine, Country country) {
        this.country = country;
        this.engine = engine;
    }

    public Country getCountry() {
        return this.country;
    }
    public Engine getEngine() {
        return this.engine;
    }
    public void setCountry(Country country) {
        this.country = country;
    }
    public void setEngine(Engine engine) {
        this.engine = engine;
    }


}
