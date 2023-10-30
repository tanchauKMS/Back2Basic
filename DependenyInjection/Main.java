package DependenyInjection;

import DependenyInjection.Country.Country;
import DependenyInjection.Country.Japan;
import DependenyInjection.Engine.Engine;
import DependenyInjection.Engine.YamahaEngine;

public class Main {
    public static void main(String[] args) {
        Engine dongCo = new YamahaEngine();
        Country country = new Japan();
        Car car = new Car(dongCo, country);
        car.getEngine().run();
        car.getCountry().getName();
        car.getCountry().getContinent();
    }
}