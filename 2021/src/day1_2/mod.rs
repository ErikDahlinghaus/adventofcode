use std::fs;

pub fn main() {
    let depth_readings = fs::read_to_string("./src/day1_2/input")
        .expect("Something went wrong reading the file");

    let no_previous = "(N/A - no previous measurement)";
    let increased = "(increased)";
    let decreased = "(decreased)";

    let mut last_depth = 0;
    let mut larger = 0;

    let mut iterator = 0;

    let length = depth_readings.split_terminator("\n").count();
    
    for depth_str in depth_readings.lines() {
        if iterator >= length-2 {
            break;
        }
        let depth0 = depth_str.parse::<i32>().unwrap();
        let depth1 = depth_readings.split_terminator("\n").nth(iterator+1).unwrap().parse::<i32>().unwrap();
        let depth2 = depth_readings.split_terminator("\n").nth(iterator+2).unwrap().parse::<i32>().unwrap();
        
        let depth = depth0 + depth1 + depth2;

        if last_depth == 0 {
            println!("{} {}", depth, no_previous);
        } else if last_depth > depth {
            println!("{} {}", depth, decreased);
        } else if depth > last_depth {
            println!("{} {}", depth, increased);
            larger = larger+1;
        } else {
            println!("depth remained the same");
        }

        last_depth = depth;
        iterator = iterator + 1;
    }

    println!("{}", larger)
}
