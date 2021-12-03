use std::fs;

pub fn main() {
    let depth_readings = fs::read_to_string("./src/day1_1/input")
        .expect("Something went wrong reading the file");

    // let no_previous = "(N/A - no previous measurement)";
    // let increased = "(increased)";
    // let decreased = "(decreased)";

    let mut last_depth = 0;
    let mut larger = 0;
    
    for depth_str in depth_readings.lines() {
        let depth = depth_str.parse::<i32>().unwrap();
        if last_depth == 0 {
            // println!("{} {}", depth, no_previous);
        } else if last_depth > depth {
            // println!("{} {}", depth, decreased);
        } else if depth > last_depth {
            // println!("{} {}", depth, increased);
            larger = larger+1;
        } else {
            // println!("depth remained the same")
        }
        last_depth = depth;
    }

    println!("{}", larger)
}
