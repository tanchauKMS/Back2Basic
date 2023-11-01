package DesignPattern.AdapterPattern;

public class JapaneseAdaptee implements LanguageAdaptee {
   public void receive(String words) {
        System.out.println("Receive word from adapter");
        System.out.println(words);
   } 
}
