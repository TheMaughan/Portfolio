import java.util.ArrayList;
public class Customer {
    String id;
    String name;
    ArrayList<Order> orders = new ArrayList<Order>();

    public Customer(String i, String n) {
        this.id = i;
        this.name = n;
    }

    public int getOrderCount() {
        // In Python I would have used a for loop, but
        //     this is much more simple:
        return orders.size();
    }

    public double grandTotal() {
        double total = 0;
        for(Order price : orders)
            total += price.getTotal();
        return total;
    }

    public void displaySummary() {
        System.out.println("Summary for customer '"+id+"'");        
        System.out.println("Customer Name: "+name);
        System.out.println("Number of orders made: "+getOrderCount());
        System.out.printf("Total: $%.2f\n",grandTotal());
    }

    public void displayReceipts() {
        System.out.println("Detailed receipt for customer '"+id+"'");
        System.out.println("Customer Name: "+name);
        System.out.println();
        for(Order i : orders){
            i.displayReceipt();
            System.out.println("--------------------------------");
        }
            
    }

}
