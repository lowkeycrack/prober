# Prober (Version 1.0)

![Prober Logo](prober-logo.png)

Prober is a command-line tool designed to probe multiple subdomains quickly and efficiently. It provides a simple yet powerful way to gather information about subdomains, making it a valuable tool for security assessments, network monitoring, and domain management.

## Features

- **Subdomain Probing:** Prober allows you to probe multiple subdomains to discover information about their existence, IP addresses, and other relevant details.

- **Customization:** You can configure Prober to suit your needs with various options, including specifying target subdomains and customizing probes.

- **User-Friendly Interface:** Prober provides an easy-to-use command line interface with clear and concise output, making it accessible to both beginners and experienced users.

- **Version Control:** Future versions of Prober are expected, with enhancements and additional features to further streamline the subdomain probing process.

## Getting Started

To get started with Prober, follow these steps:

1. **Installation:** Clone this repository and install the necessary dependencies. Detailed installation instructions can be found in the [Installation Guide](docs/installation.md).

2. **Usage:** Consult the [User Guide](docs/user-guide.md) for instructions on how to use Prober effectively.

3. **Feedback:** Your feedback is valuable! If you encounter issues or have suggestions for improvements

4. **Contributions:** Contributions are welcome! If you'd like to contribute to the development of Prober

## Future Versions

As the creator of Prober, I am committed to improving and expanding the capabilities of this tool. Expect future versions to include:

- Enhanced subdomain probing techniques.
- Improved support for various DNS record types.
- Integration with third-party APIs for additional information gathering.
- User-friendly configuration and customization options.

Stay tuned for exciting updates in the upcoming versions!
Certainly! To include the help function in your `README.md`, you can use a code block to display the output of the help command. Here's how you can do it:

```markdown
## Usage

To use Prober, follow the commands and options outlined below:

### Help

You can display the available commands and options by running:

```bash
python main.py --help
```

This will show you the main help menu, which lists available commands, such as `start`.

### Start Command

To probe subdomains, use the `start` command with the following options:

```bash
python main.py start [OPTIONS]
```

Options include:

- `-f, --filename TEXT`: Specify the filename containing the list of subdomains.
- `-t, --threads INTEGER`: Set the number of threads to use (increases the speed of the scan). The default is 10.

For detailed information on the `start` command and its options, run:

```bash
python main.py start --help
```

This will provide you with specific usage details for the subdomain probing process.

```

This Markdown section outlines how to use the Prober tool, including how to display the main help menu and how to get specific
usage details for the `start` command and its options. Users can refer to this documentation to understand how to use the tool effectively.
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*This README is written by the creator of Prober krish jha aka lowkey, and it will be regularly updated with information about new features and
improvements in upcoming versions.*
