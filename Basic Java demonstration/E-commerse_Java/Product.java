public class Product {

	// Member data:
	String id;
	String name;
	double price;
	float quantity;

	/* Constructor */
	public Product(String i, String n, double p, float q) {
		this.id = i;
		this.name = n;
		this.price = p;
		this.quantity = q;
	}

	public double getTotalPrice() {
		return this.price * this.quantity;
	}

	public void display() {
		System.out.printf("\n%s (%.0f) - $%.2f", name, quantity, getTotalPrice());
    }
}
