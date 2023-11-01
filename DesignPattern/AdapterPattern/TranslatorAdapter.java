package DesignPattern.AdapterPattern;

public class TranslatorAdapter implements ChineseTarget {
    private LanguageAdaptee adaptee;

    public TranslatorAdapter(VietnameseAdaptee adaptee) {
        this.adaptee = adaptee;
    }

    public TranslatorAdapter(JapaneseAdaptee adaptee) {
        this.adaptee = adaptee;
    }
    
    private String translate(String words) {
        System.out.println("Translated");
        return "ni hao";
    }
    
    @Override
    public void send(String words) {
        System.out.println("Receiving words from Client");
        String translatedWords = this.translate(words);
        this.adaptee.receive(translatedWords);
    }
    
}
