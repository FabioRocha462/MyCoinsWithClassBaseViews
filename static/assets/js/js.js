async function consultService(url){
    const result = await fetch(url,{
        method: 'get',
    }
    ).then(function(result){
            return result.json();
    }).then(function(data){
        const ctx = document.getElementById('despesasanuais').getContext('2d');
        var cores = gera_cor(qtd=12);
        const MyChart = new Chart (ctx,{
            type:'line',
            data:{
                labels: data["meses"],
                datasets: [{
                    label : "Despesas",
                    data : data["valores"],
                    backgroundColor: cores[0],
                    borderColor: cores[1],
                    borderWidth: 1
                }]
            },
            options:{
                scales: {
                    y : {
                        beginAtZero: true
                    }
                }
            }
        })

    });
}
function gera_cor(qtd=1){
    var bg_color = [];
    var border_color = [];
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }
    
    return [bg_color, border_color];
}
const form = document.getElementById("form_despesa");


function teste(event) {
    event.preventDefault();
    const URL = "http://127.0.0.1:8000/dashboard/despesasanuais/";
    consultService(URL);
}

async function saldo(){
    const URL = "http://127.0.0.1:8000/dashboard/valores/";
    await fetch(URL,{
        method: "get",  
    }).then(function(response){
        return response.json();
    }).then(function(data){
        const div = document.getElementById("saldo");
        div.innerHTML = `
        <div class="alert alert-success"> <h3>Seu Saldo: ${data['saldo']}</h3> </div>
        `
    });
    
}
form.addEventListener('submit', teste);
