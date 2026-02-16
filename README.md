# EDI Integration App

EDI (Electronic Data Interchange) Integration app for Dokos.

## Features

- **EDI Data Sync**: Synchronize data with external EDI systems
- **Custom DocTypes**: Support for EDI document management
- **API Integration**: Whitelisted methods for EDI operations
- **Logging**: Complete sync history and error tracking

## Installation

```bash
bench get-app dokos_lmdm_edi https://github.com/YOUR_ORG/dokos-lmdm-edi.git
bench install-app dokos_lmdm_edi
```

Or via DOKINT:
```bash
dokint app install dokos_lmdm_edi
```

## Development

Start the development server:
```bash
bench start
```

Run tests:
```bash
bench --site mysite.local run-tests --module dokos_lmdm_edi
```

## License

MIT
