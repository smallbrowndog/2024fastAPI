let MovieObject = {

    getall: function(){
      // alert("오늘의 영화 추천")
  
      $.ajax({
        type: "GET",
        url: "http://localhost:8000/all"

      }).done(function(response){
        console.log(response.result)
        let movielist = response.result
  
        // let topdiv = document.createElement("div")
        // topdiv.style = 'column-count: 5'
        // document.body.appendChild(topdiv)
        topdiv = document.getElementById("alldiv")


        // // 교수님이 알려주신 방법
        // // 익명함수
        // // movielist.array.forEach(function(movie) {
        // // 화살표 함수
        // movielist.forEach(movie=>  {
        //   cmovie = document.createElement('div')
        //   cmovie.className = 'card'
  
        //   // 이미지 가져오기
        //   mimg = document.createElement('img')
        //   mimg.className = 'card-img-top'
        //   mimg.src = movie.poster_path

        //   // 이미지 클릭 시 이벤트 생성
        //   mimg.onclick = function(){
        //     // 교수님이 알려주신 방식
        //     window.location.href = movie.url
        //     // 새 창에서 영화 URL 열기
        //     // window.open(movie.url, '_blank');
        //   }        
  
        //   cmovie.appendChild(mimg)
        //   topdiv.appendChild(cmovie)
            
        // });
  
        for (let i = 0; i < 10; i++) {
          let cmovie = document.createElement('div')
          cmovie.className = 'card'
  
          // 이미지 가져오기
          let mimg = document.createElement('img')
          mimg.className = 'card-img-top'
          mimg.src = movielist[i].poster_path

          // 이미지 클릭 시 이벤트 생성
          mimg.onclick = function(){
            // 새 창에서 영화 URL 열기
            window.open(movielist[i].url, '_blank');
          }
  
          cmovie.appendChild(mimg)
          topdiv.appendChild(cmovie)

          // 마우스 오버 효과
          mimg.onmouseover = function(){
            // 이미지 밝기 변경
            mimg.style.filter = "brightness(150%)";
            // 커서 모양 변경
            document.body.style.cursor = "pointer";
          }
          mimg.onmouseout = function(){
            // 이미지 밝기 원래대로 변경
            mimg.style.filter = "brightness(100%)";
            // 커서 모양 원래대로 변경
            document.body.style.cursor = "default";
          }
        }
  
      }).fail();
    },

    getgenres: function(){
      // alert("장르 추천")

      // 앞 html에서 옵션값 가져오기
      genre = document.getElementById("sgenre").value.toLowerCase()
      
      $.ajax({
        type: "GET",
        url: "http://localhost:8000/genres/" + genre

      }).done(function(response){
        console.log(response.result)
        let movielist = response.result

        genrediv = document.getElementById("genrediv")
        // 1. 기존의 영화 삭제하기
        // genrediv.innerHTML = ""
        
        // 2. 아래에서 appendChild를 사용한것처럼 removeChild를 사용한다
        // if를 사용하면 1개만 삭제해서 10개, 19개, 28개, 37개, .... 가 되기때문에 while를 작성해야함
        while (genrediv.firstChild){
          genrediv.removeChild(genrediv.firstChild)
        }
        

        for (let i = 0; i < 10; i++) {
          let cmovie = document.createElement('div')
          cmovie.className = 'card'
  
          // 이미지 가져오기
          let mimg = document.createElement('img')
          mimg.className = 'card-img-top'
          mimg.src = movielist[i].poster_path

          // 이미지 클릭 시 이벤트 생성
          mimg.onclick = function(){
            // 새 창에서 영화 URL 열기
            window.open(movielist[i].url, '_blank');
          }
  
          cmovie.appendChild(mimg)
          genrediv.appendChild(cmovie)

          // 마우스 오버 효과
          mimg.onmouseover = function(){
            // 이미지 밝기 변경
            mimg.style.filter = "brightness(150%)";
            // 커서 모양 변경
            document.body.style.cursor = "pointer";
          }
          mimg.onmouseout = function(){
            // 이미지 밝기 원래대로 변경
            mimg.style.filter = "brightness(100%)";
            // 커서 모양 원래대로 변경
            document.body.style.cursor = "default";
          }
        }
  
      }).fail();
    },
    getitems: function(){
      // alert("오늘의 영화 추천")

      itemid = document.getElementById("itemid").value
  
      $.ajax({
        type: "GET",
        url: "http://localhost:8000/item-based/" + itemid

      }).done(function(response){
        console.log(response.result)
        let movielist = response.result

        itemdiv = document.getElementById("itemdiv")

        while (itemdiv.firstChild){
          itemdiv.removeChild(itemdiv.firstChild)
        }
  
        for (let i = 0; i < 10; i++) {
          let cmovie = document.createElement('div')
          cmovie.className = 'card'
  
          // 이미지 가져오기
          let mimg = document.createElement('img')
          mimg.className = 'card-img-top'
          mimg.src = movielist[i].poster_path

          // 이미지 클릭 시 이벤트 생성
          mimg.onclick = function(){
            // 새 창에서 영화 URL 열기
            window.open(movielist[i].url, '_blank');
          }
  
          cmovie.appendChild(mimg)
          itemdiv.appendChild(cmovie)

          // 마우스 오버 효과
          mimg.onmouseover = function(){
            // 이미지 밝기 변경
            mimg.style.filter = "brightness(150%)";
            // 커서 모양 변경
            document.body.style.cursor = "pointer";
          }
          mimg.onmouseout = function(){
            // 이미지 밝기 원래대로 변경
            mimg.style.filter = "brightness(100%)";
            // 커서 모양 원래대로 변경
            document.body.style.cursor = "default";
          }
        }
  
      }).fail();
    },


    getrating: function(){
      // alert("오늘의 영화 추천")

      movieNrating = document.getElementById("movieNrating").value
      
  
      $.ajax({
        type: "GET",
        url: "http://localhost:8000/user-based/?params=" + movieNrating

      }).done(function(response){
        console.log(response.result)
        let movielist = response.result

        userdiv = document.getElementById("userdiv")

        while (userdiv.firstChild){
          userdiv.removeChild(userdiv.firstChild)
        }
  
        for (let i = 0; i < 10; i++) {
          let cmovie = document.createElement('div')
          cmovie.className = 'card'
  
          // 이미지 가져오기
          let mimg = document.createElement('img')
          mimg.className = 'card-img-top'
          mimg.src = movielist[i].poster_path

          // 이미지 클릭 시 이벤트 생성
          mimg.onclick = function(){
            // 새 창에서 영화 URL 열기
            window.open(movielist[i].url, '_blank');
          }
  
          cmovie.appendChild(mimg)
          userdiv.appendChild(cmovie)

          // 마우스 오버 효과
          mimg.onmouseover = function(){
            // 이미지 밝기 변경
            mimg.style.filter = "brightness(150%)";
            // 커서 모양 변경
            document.body.style.cursor = "pointer";
          }
          mimg.onmouseout = function(){
            // 이미지 밝기 원래대로 변경
            mimg.style.filter = "brightness(100%)";
            // 커서 모양 원래대로 변경
            document.body.style.cursor = "default";
          }
        }
  
      }).fail();
    }
  }
  
  MovieObject.getall()
