public class Main {
  public static void main(String[] args) {
    // Selecting Products 1:
		Product p1 = new Product("1238223", "Sword", 1899.99, 10);
    p1.getTotalPrice();
    // Select product 2:
    Product p2 = new Product("838ab883", "Shield", 989.75, 6);
    p2.getTotalPrice();
    // Make order 1:
    Order order1 = new Order("1138");
    order1.products.add(p1);
    order1.products.add(p2);
    order1.getSubtotal();
    // System produces a receipt:
    System.out.println();
    System.out.println("### Testing Customers ###");
    Customer c = new Customer("aa32", "Gandalf");
    c.orders.add(order1);
    c.displaySummary();
    c.displayReceipts();
    // Another order is made and the system adds all orders to one invoice for customer:
    Product p3 = new Product("2387127", "The Ring", 1000000, 1);
    Product p4 = new Product("1828191", "Wizard Staff", 199.99, 3);
    Order order2 = new Order("1277182");
    order2.products.add(p3);
    order2.products.add(p4);
    c.orders.add(order2);
    c.displaySummary();
    c.displayReceipts();
  }
}
  