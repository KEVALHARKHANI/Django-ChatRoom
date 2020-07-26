var formdata=document.getElementById('form1');

console.log(window.location)
        var video2= document.getElementById('video2')
        var msg=document.getElementById('msg')
        var display=document.getElementById('display')
        var formdata=document.getElementById('form1')
        var wsStart = 'ws://'
        var endpoint=wsStart+window.location.host + window.location.pathname
        var socket= new WebSocket(endpoint)




        socket.onmessage = function(e){
            console.log("message",e)
            var r_data=JSON.parse(e.data)
            if(r_data.user){
            if(r_data.disconnected){
                var user=document.getElementById(r_data.user)
                user.remove();
            }else{
            var user_exist=document.getElementById(r_data.user)
            if(!user_exist){
            console.log("active user "+r_data.user)
            var user=document.getElementById('user')
            var li = document.createElement("LI");
            user.appendChild(li);
            li.id=r_data.user;
            li.innerHTML=r_data.user;
            }
}

            }
            else{
            if(r_data.username=="{{request.user}}"){
            var insert=document.getElementById('msg');
            insert.innerHTML=insert.innerHTML+
            "{%my_msg r_data.message r_data.url r_data.datetime %}"
            }else{
             var insert=document.getElementById('msg');
            insert.innerHTML=insert.innerHTML+
            "{%other_msg r_data.message r_data.url r_data.datetime %}"
             }
            var myDiv = document.getElementById("first-div");
            myDiv.scrollTop = myDiv.scrollHeight;

            }
        }
        socket.onopen =  function(e){
            console.log("open",e)
            formdata.onsubmit=function(event){
            event.preventDefault()
            console.log('send:'+msg.value)
            socket.send(msg.value)
            msg.value="";
            }

        }
        socket.onerror =  function(e){
            console.log("error:",e)
        }
        socket.onclose =  function(e){
            console.log("closed ",e)
        }

        function vc(){
        var video= document.getElementById('video')

        if (navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
          video.srcObject = stream;
          console.log(stream)
        socket.send(stream)
        })
        .catch(function (err0r) {
          console.log("Something went wrong!");
        });
    }
        }