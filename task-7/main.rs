use std::io;
extern crate regex;
use regex::Regex;

fn main() {
	while 1>0 {
			let mut email = String::new();
			println!("{}", "Enter email:");
			match io::stdin().read_line(&mut email) {
        		Ok(_) => {}
        		Err(e) => println!("error: {}", e)
    		}
    		let regex = Regex::new(r"^([a-z0-9_+]([a-z0-9_+.]*[a-z0-9_+])?)@([a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,6})").unwrap();
    		if regex.is_match(&email) {
    			println!("{}", "is a valid email id")
    		}
    		else {
    			println!("{}", "is not a valid email id")
    
			}
		}
}