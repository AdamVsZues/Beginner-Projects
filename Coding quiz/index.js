let score = 10;
const question = document.getElementsByClassName('question');

function grade(){
        correct = document.getElementsByClassName('Qa');
        
        for (let index = 0; index < correct.length; index++) {
            
            
            if (correct[index].checked){
                document.getElementById('question' + index).style.backgroundColor = '#1EFC1E'
                document.getElementById('question' + index).style.borderRadius = '50px'
            } else{
                document.getElementById('question' + index).style.backgroundColor = '#ff184c'
                document.getElementById('question' + index).style.borderRadius = '50px'
                score --;
                console.log(score)
            }
            document.querySelector('#submit').disabled = true;

            scorebox = document.getElementById('scorebox')
            document.getElementById('score').innerHTML = (score + '/10')

            scorebox.style.display = 'inline-block'

        }
    }
    // try{
        // let ans = document.getElementsByName('Q1');

// for(i = 0; i < ans.length; i++) {
//                 if(ans[i].checked)
//                 alert(ans[i].value);
//             }

// catch(err)

// {

//     alert("Please fill in the answer");

// }
//}