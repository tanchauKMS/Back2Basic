public class Main {
    public static void main(String[] args) {
            Food meal = FoodFactory.getFood(FoodType.MEAT);
            System.out.println("Today meal is " + meal.getFoodName());
    }
}
