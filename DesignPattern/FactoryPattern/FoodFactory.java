public class FoodFactory {
    private FoodFactory() {}
    public static final Food getFood(FoodType type) {
        switch (type) {
            case MEAT:
                return new Meat();
            case VEGETABLE:
                return new Vegetable();
            default:
                return (Food) new IllegalArgumentException("Food type is not defined");
        }
    }
}
