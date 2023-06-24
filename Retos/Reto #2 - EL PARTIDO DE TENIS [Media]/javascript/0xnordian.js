const points = new Map([
  [0, "Love"],
  [1, "15"],
  [2, "30"],
  [3, "40"],
]);

function tenisGame(arr) {
  let p1 = 0;
  let p2 = 0;
  arr.map(item => (item !== "P1" && item !== "P2") ? (() => { throw new Error("Wrong input. You can only enter 'P1' or 'P2' as values"); })() : "");
  for(let i = 0; i < arr.length; i++) {
    arr[i] === "P1" ? p1++ : p2++;
    if(p1 >= 3 && p2 >= 3){
      if(p1 === p2) {
        console.log("Deuce")
      } else if ((p1 - p2 === 1) || (p2 - p1 === 1)){
        p1 > p2 ? console.log("Ventaja P1") : console.log("Ventaja P2")
      } else if((p1 - p2 >= 2) || (p2 - p1 >= 2)){
        if(p1 > p2){
          console.log("Ha ganado el P1");
          break;
        } else {
          console.log("Ha ganado el P2");
          break;
        }
      } 
    } else {
        console.log(`${points.get(p1)} - ${points.get(p2)}`);
    }
  }
}
