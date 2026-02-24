/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.*;
public class Main
{
	public static void main(String[] args) {
		System.out.println("Temperatura registrada");
		Scanner leer = new Scanner(System.in);
		//nextline es para String
		//NextFloat es para Leer decimales
		float temp = leer.nextFloat();
		// &&(and)  ||(or)
		if (temp>=27){System.out.println("Ponte algo fresco");}
		else if(temp>=20 && temp<27){System.out.println("Abrigate");}
	
		
		//Ejercicio para easy hand if
		System.out.println("Cual es tu edad?");
		int edad = leer.nextInt();
		System.out.println(edad>=18? "Eres mayor de edad":"No eres mayor de edad");
		
		
		
	}
}