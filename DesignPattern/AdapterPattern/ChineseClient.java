package DesignPattern.AdapterPattern;

public class ChineseClient {
    public static void main(String[] args) {
        ChineseTarget client = new TranslatorAdapter(new JapaneseAdaptee());
        client.send("Konnichiwa");

        ChineseTarget client2 = new TranslatorAdapter(new VietnameseAdaptee());
        client2.send("Xin chào");
    }
}
