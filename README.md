# WebStuff

A Python-based asynchronous web utility toolkit that provides various web-related functionalities including header management, URL building, and logging capabilities.

## Features

- Asynchronous web operations using `aiohttp`
- Custom header management
- URL building utilities
- Advanced logging functionality
- Debug tools

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/louisgoodenws/WebStuff.git
cd WebStuff
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The main entry point is `main.py`. Run it using:

```bash
python main.py
```

## Project Structure

- `main.py`: Main entry point for the application
- `headers.py`: Header management utilities
- `url_builder.py`: URL construction and manipulation tools
- `logger.py`: Logging configuration and utilities
- `level.py`: Level management
- `debug.py`: Debugging utilities
- `web_service`: Web service implementation

## License

This project is licensed under the terms included in the LICENSE file.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Last Updated

2024-12-11