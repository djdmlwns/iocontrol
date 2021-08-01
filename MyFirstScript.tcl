# set variable number 22
set val 22

for {set i 0} {$i < 6} {incr i} {
    # expr is to calculate
    set val [expr {$val * 3}]  
}

if {$val > 20000} {
    puts "The value of val is $val"
} else {
    puts "The value $val is less than 20,000"
}

