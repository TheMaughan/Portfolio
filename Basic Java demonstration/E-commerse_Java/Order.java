import java.util.ArrayList;
public class Order {
    String id;
    ArrayList<Product> products = new ArrayList<Product>();

    public Order(String i) {
        this.id = i;
    }

    public double getSubtotal() {
        double orderSubtotal = 0;
        for(Product i : products)
            orderSubtotal += i.getTotalPrice();
        
        return orderSubtotal;
    }

    public double getTax() {
        return getSubtotal() * 0.065;
    }

    public double getTotal() {
        return getSubtotal() + getTax();
    }

    public void displayReceipt() {
        System.out.printf("Order: %s", this.id);
        
        for(Product i : products)
            i.display();
        
        System.out.printf("\nSubtotal: $%.2f",getSubtotal());
        System.out.printf("\nTax: $%.2f",getTax());
        System.out.printf("\nTotal: $%.2f\n",getTotal());
    }

    
}
