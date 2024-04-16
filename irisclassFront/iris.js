google.charts.load("current", {packages:["corechart"]});
// google.charts.setOnLoadCallback(drawChart);

function drawChart(p) {
  var data = google.visualization.arrayToDataTable([
    ['iris', 'species'],
    ['setosa',     p[0]],
    ['versicolor', p[1]],
    ['virginica',  p[2]]
  ]);

  var options = {
    title: '붓꽃 예측 결과',
    is3D: true,
  };

  var chart = new google.visualization.PieChart(document.getElementById('piechart_3d'));
  chart.draw(data, options);
}

function Send(){

    sl = document.getElementById("sl")
    sw = document.getElementById("sw")
    pl = document.getElementById("pl")
    pw = document.getElementById("pw")
    
      var data = {
        'sepal_length': sl.value,
        'sepal_width': sw.value,
        'petal_length': pl.value,
        'petal_width': pw.value,
      }  
    
      $.ajax({
        type: "POST",
        url: 'http://localhost:8000/predict',
        headers:{
            "Accept" : "application/json",
            "Content-Type": "application/json", 
            },
        data: JSON.stringify(data),
    
      }).done(function(response) {
    
            txtOut.value = response.predict + "  " + response.probability
    
            console.log(response)

            rp = response.probability

            p = [rp[0][0], rp[0][1], rp[0][2]]
            // 데이터가 정상적으로 불러들어와질때 표가 뜨도록 변경
            google.charts.setOnLoadCallback(drawChart(p));
    
    
      }).fail(function(error) {
        alert("!/js/.js에서 에러발생: " + error.statusText);
        console.log(error)
      }).always(function(r){
        console.log("always" + r)
      });
    
    
    }