<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="style.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="index.js"></script>
    <title>vs project</title>
</head>

<body>
    <h1 class="heading">Welcome to the Rock , Paper, scissor game</h1>
    <h3 class="welcome">Welcome </span class="name">"name"</span></h3>
    <div class="game">
        <p class="clash comp">computer</p>
        <p class="clash vs">vs</p>
        <p class="clash you">you</p>
    </div>
    <div class="chooseany">
        <img src="rock.jpg" alt="Rock" class="rock choose" id="rock">
        <img src="paper cropped.jpg" alt="paper" class="paper choose" id="apper">
        <img src="scissors .jpg" alt="scissors" class="scissor choose" id="scissor">
        <!-- <p class="rock choose">rock</p>
        <p class="paper choose">paper</p>
        <p class="scissor choose">scissor</p> -->

    </div>
    <div class="symbol">
        <p id="comp">symbol what the computer chose</p>
        <p class="user"> symbol what the user chose</p>
    </div>

    <div class="winner">
        <p> the winner is</p>
    </div>


    <script>

        var name = prompt("what is name buddy? ")
        user.innerHTML = name;

        const rock = document.querySelector('.rock');
        const paper = document.querySelector('.paper')
        const scissor = document.querySelector('.scissor');
        const winner = document.querySelector('.winner')
        const user = document.querySelector("name")

        document.addEventListener('click', () => {



        })



        function sps(t) {
            var comp;
            if (t < 3) {
                comp = 'r';
            }
            else if (t > 3 && t < 6) {
                comp = 'p';
            }
            else {
                comp = 's';
            }
            return comp;
        }
        function winner(you, comp) {
            if (you == comp) {
                return 0;
            }
            else if (you == 's' && comp == 'r') {
                return -1;
            }
            else if (you == 's' && comp == 'p') {

                return 1;
            }
            else if (you == 'p' && comp == 'r') {

                return 1;
            }
            else if (you == 'p' && comp == 's') {

                return -1;
            }
            else if (you == 'r' && comp == 'p') {
                return -1;
            }
            else if (you == 'r' && comp == 's') {
                return 1;
            }
        }
        function answer(x) {
            if (x == 0) {
                cout << "game draw !" << endl;
            }
            else if (x == 1) {
                cout << "you won !" << endl;
            }
            else {
                cout << "you lose !" << endl;
            }
        }
        function main() {
            var u = 100;
            while (u--) {

                cout << "please enter 'r' for rock , 'p' for paper and 's' for scissor : ";
                let you, comp;
                cin >> you;
                srand(time(0));
                let number = rand() % 10 + 1;
                comp = sps(number);
                let result = winner(you, comp);
                // int t = rand(100);
                cout << "you chose " << you << " and the computer chose " << comp << " , hence" << endl;
                answer(result);
                // cout<<you<<" "<<comp;
            }


            return 0;
        }


    </script>
</body>


</html>
