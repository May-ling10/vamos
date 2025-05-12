<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Feliz Día de las Madres</title>
  <style>
    body {
      margin: 0;
      font-family: 'Segoe UI', sans-serif;
      background: #fff0f5;
      color: #333;
      text-align: center;
    }

    header {
      background-color: #ff69b4;
      color: white;
      padding: 2rem;
      font-size: 2rem;
    }

    .section {
      padding: 2rem;
    }

    .gallery {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 1rem;
    }

    .gallery img {
      width: 100%;
      max-width: 200px;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    video {
      width: 90%;
      max-width: 600px;
      border-radius: 10px;
    }

    .message {
      font-size: 1.2rem;
      margin-top: 1rem;
    }

    @media (max-width: 600px) {
      header {
        font-size: 1.5rem;
      }
    }
  </style>
</head>
<body>
  <header>
    💐 ¡Feliz Día de las Madres! 💐
  </header>

  <section class="section">
    <h2>🌷 Nuestra Galería</h2>
    <div class="gallery">
      <img src="foto1.jpg" alt="Foto 1">
      <img src="foto2.jpg" alt="Foto 2">
      <img src="foto3.jpg" alt="Foto 3">
    </div>
  </section>

  <section class="section">
    <h2>🎥 Video Especial</h2>
    <video controls>
      <source src="video_mama.mp4" type="video/mp4">
      Tu navegador no soporta video HTML5.
    </video>
  </section>

  <section class="section">
    <h2>💌 Un Mensaje para Ti</h2>
    <p class="message">
      Mamá, gracias por tu amor incondicional, por cada abrazo, por tu apoyo constante y por ser la mejor del mundo. ¡Te amo mucho!
    </p>
  </section>
</body>
</html>
