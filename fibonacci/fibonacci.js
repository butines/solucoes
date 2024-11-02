function fibonacci(n){
    if(n<0) return false;

    let a=0, b=1;
    while(a<n){
        [a,b] = [b,a + b];
    }

    return a === n;
}

const num = 8;

if(fibonacci(num)){
    console.log(`O número ${num} faz parte da sequência de Fibonacci.`);
}

else{
    console.log (`O número ${num} não faz parte da sequência de Fibonacci.`);
}