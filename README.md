# OpenAI Realtime API + Twilio Voice Integration

A powerful integration that combines OpenAI's Realtime API with Twilio's Voice services to create interactive voice calls with AI responses. This project enables real-time voice conversations between humans and AI, making it perfect for compliance monitoring, customer service automation, and other voice-based AI applications.

- AI sales agent
- AI Support Agent
- AI Cold Calling
- AI Compliance

## Features

- Real-time voice streaming between Twilio and OpenAI
- Automatic speech detection and response cancellation
- Configurable voice settings and system prompts
- Environment-based configuration
- WebSocket-based communication
- Support for G711 ULAW audio format
- Interrupt handling for natural conversation flow
- Session management and real-time updates

## Prerequisites

Before you begin, ensure you have:

- Python 3.8 or higher
- An OpenAI API key with Realtime API access
- A Twilio account with:
  - Account SID
  - Auth Token
  - Phone Number
- ngrok or similar tool for exposing local server to the internet

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rehan-dev/ai-call-agent.git
cd ai-call-agent
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your credentials:
```env
OPENAI_API_KEY=your_openai_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
NGROK_URL=your_ngrok_url
PORT=5050
```

## Usage

1. Start the server:
```bash
uvicorn main:app --port 5050
```

2. Expose your local server using ngrok:
```bash
ngrok http 5050
```

3. Update your Twilio Voice webhook URL to point to your ngrok URL + `/outgoing-call`

4. Make a call using the API endpoint:
```bash
curl -X POST "http://localhost:5050/make-call" -H "Content-Type: application/json" -d '{"to_phone_number": "+1234567890"}'
```

## Project Structure

```
.
├── main.py              # Main application file
├── prompts/            
│   └── system_prompt.txt # System instructions for AI
├── requirements.txt     # Python dependencies
├── .env                # Environment variables
├── .gitignore          # Git ignore file
├── LICENSE             # License file
└── README.md           # Project documentation
```

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key
- `TWILIO_ACCOUNT_SID`: Your Twilio Account SID
- `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token
- `TWILIO_PHONE_NUMBER`: Your Twilio phone number
- `NGROK_URL`: Your ngrok URL
- `PORT`: Server port (default: 5050)

### System Prompt

The AI's behavior can be customized by modifying the system prompt in `prompts/system_prompt.txt`.

## API Endpoints

- `GET /`: Health check endpoint
- `POST /make-call`: Initiate a new call
- `POST /outgoing-call`: Webhook for Twilio voice calls
- `WebSocket /media-stream`: WebSocket endpoint for media streaming

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Vladyslav P.**

## Acknowledgments

- OpenAI for providing the Realtime API
- Twilio for their excellent voice services
- The open-source community for inspiration and support

## Disclaimer

This project is not officially affiliated with OpenAI or Twilio. Use at your own risk.
