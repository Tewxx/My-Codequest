import java.util.Scanner;
public class ChineseZodiac {
    public static void main(String[] args) {
        Scanner ScanScanner = new Scanner(System.in);
        int Scan1 = ScanScanner.nextInt();
        for (int i = 0; i < Scan1; i++) {
            int Year = ScanScanner.nextInt();
            String EvenOrOdd;
            // Step 1 Yang/Yin
            if(Year % 2 == 0) {
                EvenOrOdd = ("Yang");
            } else {
                EvenOrOdd = "Yin";
            }

            // Step 2 Element
            var Minus4 = Year-4;
            var Step2Part1 = Minus4%10;
            var Step2Part2 = Step2Part1/2;
            var Step2Part3 = (Math.round(Step2Part2));
            String Element="";
            if(Step2Part3 == 0) {
                Element = "Wood";
            }
            if(Step2Part3 == 1) {
                Element = "Fire";
            }
            if(Step2Part3 == 2) {
                Element = "Earth";
            }
            if(Step2Part3 == 3) {
                Element = "Metal";
            }
            if(Step2Part3 == 4) {
                Element = "Water";
            }

            // Step 3 Animal
            String Animal = "";
            var Step3Part1 = Minus4%12;
            if(Step3Part1 == 0) {
                Animal = "Rat";
            }
            if(Step3Part1 == 1) {
                Animal = "Ox";
            }
            if(Step3Part1 == 2) {
                Animal = "Tiger";
            }
            if(Step3Part1 == 3) {
                Animal = "Rabbit";
            }
            if(Step3Part1 == 4) {
                Animal = "Dragon";
            }
            if(Step3Part1 == 5) {
                Animal = "Snake";
            }
            if(Step3Part1 == 6) {
                Animal = "Horse";
            }
            if(Step3Part1 == 7) {
                Animal = "Goat";
            }
            if(Step3Part1 == 8) {
                Animal = "Monkey";
            }
            if(Step3Part1 == 9) {
                Animal = "Rooster";
            }
            if(Step3Part1 == 10) {
                Animal = "Dog";
            }
            if(Step3Part1 == 11) {
                Animal = "Pig";
            }

            System.out.println(Year+" "+EvenOrOdd+" "+Element+" "+Animal);

        }

    }
}
