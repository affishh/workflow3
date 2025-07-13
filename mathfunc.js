function is_even(num) {
    return num % 2 ==0;
}

function is_odd(num){
    return is_even(num);
}

function add(a, b){
    return a + b;
}

function subtract(a, b){
    return a - b;
}

function multiply(a, b){
    return a * b;
}

function divide(a, b){
    if(b==0){
        throw new Error("division by zero not allowed")
    }
}

module.exports = {
    is_even,
    is_odd,
    add,
    subtract,
    multiply,
    divide
}; 

