/// Question 1:-
// let nums= [1,2,3,4,5,6,7,8,9,10];
// nums.map ((num) => {
//   return num**2; 
// });


/// Question 2:-
// function getGrade(score) {
//     return score >= 90 ? 'A' :
//            score >= 80 ? 'B' :
//            score >= 70 ? 'C' :
//            score >= 60 ? 'D' : 'F';
// }


/// Question 3:-
// const car = {
//     companyName: "Toyota",
//     model: "Corolla",
//     year: 2020
// };
// function changeCarYear(carObject, newYear) {
//     carObject.year = newYear;
// }r
// changeCarYear(car, 2023);
// const { model, year } = car;
// console.log(`Model: ${model}, Year: ${year}`);
// console.log(car);


/// Question 4:-
// function isPrime(num) {
//     if (num < 2) return false;
//     for (let i = 2; i <= Math.sqrt(num); i++) {
//         if (num % i === 0) return false;
//     }
//     return true;
// }
// const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15];
// const primeNumbers = numbers.filter(isPrime);
// console.log(primeNumbers);


///Question 5:-
// Data cleaning: You can use map(), filter(), and reduce() to clean up data. For example, you can use map() to extract email addresses from a list of dictionaries, filter() to remove empty strings, and set() to remove duplicates. 
// Data processing: You can use map(), filter(), and reduce() to process data in diverse ways. 
// Functional programming: You can use map(), filter(), and reduce() to perform operations by passing functions inside other functions.


///Question 6:-
// async function fetchData() {
//     try {
//       const url = 'https://jsonplaceholder.typicode.com/posts';
//       const response = await fetch(url);
//       if (!response.ok) {
//         throw new Error(`HTTP error! Status: ${response.status}`);
//       }
//       const data = await response.json();
//       console.log(data);
//     } catch (error) {
//       console.error('Error fetching data:', error.message);
//     }
// }
// fetchData();


///Question 7:-
// const person = {
//     name: "Pedry",
//     address: {
//       street: "123 Elm Street",
//       city: "Metropolis",
//       zip: "713379"
//     },
//     contact: {
//       email: "pedrick9811@gmail.com",
//       phone: "555-1234"
//     }
//   };
// const phoneNumber = person.contact?.phone;
// console.log(phoneNumber);