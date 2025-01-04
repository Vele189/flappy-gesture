# FlappyHand 🖐️

A gesture-controlled version of Flappy Bird that lets you play using hand movements through your webcam! Open your palm to make the bird fly up, close your fist to let it fall.

## Features 🎮

- Hand gesture controls using webcam input
- Real-time hand tracking powered by MediaPipe
- Classic Flappy Bird gameplay mechanics
- Pixel-perfect art style
- Sound effects and visual feedback
- Cross-browser compatibility

## Tech Stack 🛠️

### Backend
- Python 3.8+
- MediaPipe for hand tracking
- WebSocket server for real-time communication

### Frontend
- React
- HTML5 Canvas for rendering
- WebSocket client
- Pixel art assets

## Prerequisites 📋

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Node.js 14.0 or higher
- npm or yarn
- Webcam
- Modern web browser

## Installation 🔧

1. Clone the repository
```bash
git clone [https://github.com/yourusername/flappy-hand.git](https://github.com/Vele189/flappy-gesture.git
cd flappy-gesture
```

2. Set up the backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

3. Set up the frontend
```bash
cd frontend
npm install
npm start
```

4. Open your browser and navigate to `http://localhost:3000`

## How to Play 🎯

1. Allow camera access when prompted
2. Position yourself so your hand is visible to the camera
3. Use these gestures to control the bird:
   - Open hand ✋ : Bird flies up
   - Closed fist ✊ : Bird falls down
4. Avoid pipes and collect points
5. Try to beat your high score!

## Project Structure 📁

```
FlappyHand/
├── backend/          # Python backend with MediaPipe
├── frontend/         # React frontend
│   ├── src/
│   │   ├── assets/  # Game assets (sprites, sounds)
│   │   ├── core/    # Game logic
│   │   ├── controls/# Hand tracking integration
│   │   └── ui/      # Game rendering and display
```

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 👏

- Original Flappy Bird game by Dong Nguyen
- MediaPipe by Google

