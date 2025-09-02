# Friday AI Assistant 🤖

> *"Will do, Sir" - Your personal AI butler with a touch of sass*

A sophisticated multimodal AI assistant inspired by Iron Man's Friday, built with real-time voice interaction, computer vision, persistent memory, and extensible tool integration.

## ✨ Key Features

### 🎭 **Butler Personality**
- Classy, sarcastic responses with proper acknowledgments
- One-sentence replies for snappy interactions
- Context-aware conversations with personality consistency

### 🧠 **Persistent Memory System**
- Remembers conversations across sessions using Mem0
- Personalized greetings based on conversation history
- Smart follow-up questions on open topics

### 👁️ **Multimodal Capabilities**
- **Voice**: Real-time speech recognition and synthesis
- **Vision**: Computer vision for visual input analysis
- **Text**: Natural language processing and understanding

### 🛠️ **Extensible Tool Integration**
- **Weather**: Real-time weather data via wttr.in
- **Web Search**: DuckDuckGo integration for web queries
- **Spotify**: Complete music control (search, queue, play, skip)
- **MCP Protocol**: Extensible tool system for future integrations

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   LiveKit       │    │   OpenAI         │    │   Mem0          │
│   (Voice/Video) │◄──►│   (RealtimeModel)│◄──►│   (Memory)      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Friday Assistant                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │
│  │   Tools     │  │   Prompts   │  │      MCP Server         │ │
│  │             │  │             │  │   (N8N Integration)     │ │
│  │ • Weather   │  │ • Persona   │  │                         │ │
│  │ • Search    │  │ • Session   │  │ • Extensible Tools      │ │
│  │ • Spotify   │  │ • Memory    │  │ • Custom Workflows      │ │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites
```bash
# Required API keys and services
- OpenAI API key
- LiveKit credentials
- Mem0 configuration
- Spotify API credentials (optional)
- N8N MCP Server URL (optional)
```

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/friday-ai-assistant.git
cd friday-ai-assistant

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# Run the assistant
python agent.py
```

### Environment Setup
```bash
# .env file
OPENAI_API_KEY=your_openai_key
LIVEKIT_URL=your_livekit_url
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_secret
N8N_MCP_SEVER_URL=your_n8n_mcp_server_url
```

## 🎯 Usage Examples

### Voice Commands
```
👤 "Friday, what's the weather in New York?"
🤖 "It's 72°F and sunny in New York, quite pleasant for your standards, Sir."

👤 "Can you search for AI news?"
🤖 "Will do, Boss. Here are the latest AI developments..."

👤 "Play some jazz music"
🤖 "Of course Sir, queuing up some sophisticated tunes for you."
```

### Visual Input
- Show objects for counting or identification
- Display documents for analysis
- Present images for description or questions

## 🧩 Core Components

### `agent.py` - Main Assistant Logic
- Agent initialization with personality and tools
- Memory management and persistence
- Session handling and shutdown hooks
- MCP server integration

### `prompts.py` - Personality & Instructions
- Butler persona definition with sarcasm
- Tool-specific instructions (especially Spotify)
- Memory handling guidelines
- Session management instructions

### `tools.py` - Utility Functions
- Weather data retrieval
- Web search capabilities
- Error handling and logging

## 🎵 Spotify Integration

The assistant provides comprehensive Spotify control:

```python
# Search and queue songs
"Friday, add 'Bohemian Rhapsody' to my queue"

# Play specific tracks
"Play some Beatles music"

# Control playback
"Skip to the next song"
```

## 🧠 Memory System

Friday remembers your conversations and provides personalized interactions:

```json
{
  "memory": "Abdullah got the job",
  "updated_at": "2025-08-24T05:26:05.397990-07:00"
}
```

The assistant uses this context for:
- Personalized greetings
- Following up on previous conversations
- Avoiding repetitive questions
- Building conversational context

## 🔧 Extensibility

The MCP (Model Context Protocol) integration allows for easy tool expansion:
- Connect to N8N workflows
- Add custom business logic
- Integrate with external services
- Create domain-specific tools

## 🏆 Technical Highlights

- **Real-time Processing**: LiveKit for low-latency voice/video
- **Multimodal AI**: OpenAI's Realtime Model for voice + vision
- **Memory Persistence**: Async memory client with user-specific storage
- **Tool Architecture**: Function-based tools with proper error handling
- **Personality System**: Consistent character responses with context awareness

## 🚧 Future Enhancements

- [ ] Mobile app integration
- [ ] Smart home device control
- [ ] Calendar and email management
- [ ] Advanced computer vision tasks
- [ ] Multi-language support
- [ ] Custom voice training

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by Iron Man's Friday AI assistant
- Built following best practices in AI agent development
- Special thanks to the open-source community for the amazing tools and libraries

---

⭐ **Star this repository if you found it helpful!**
