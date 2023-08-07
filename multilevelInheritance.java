package inheritance;


class Circle{
	public float pi=3.14f;
	public float circlearea=0f;
	
	public float calculateCricleArea(int radius) {
		return circlearea=2*pi*radius;		
	}
}
class Triangle extends Circle{
	
	  public float calculateTriangleArea(int base , int height) {
		  float triangleArea=0f;
		  
		   triangleArea=(float) ((0.5*(base*height)));
		   return triangleArea;
		   
	  }
}
class Tester{
	public static void main(String args[]) {
		Triangle t=new Triangle();
		System.out.println(t.calculateCricleArea(12));
		System.out.print(t.calculateTriangleArea(12,15));
	}
}
