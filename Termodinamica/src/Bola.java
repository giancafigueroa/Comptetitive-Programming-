import java.awt.Point;

public class Bola {
	Point bola;
	int decicion;
	public Bola(int x, int y ,int dirigo) {
		this.bola= new Point(x, y);
		this.decicion=dirigo;
	}
}