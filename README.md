![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)

# Satoshi-Guard

Welcome to Satoshi-Guard, a robust and intuitive crypto custody solution designed to streamline the management of your crypto accounts, wallets, and transactions with ease and security. Satoshi-Guard offers a modular monolithic architecture poised for potential evolution into a microservices-based application.
Our solution caters to both individuals and enterprises looking to enhance their cryptocurrency management processes.

### Project Structure Overview


- **/ci:** Contains continues integration settings and files.
- **/modules:** Contains domain-specific logic grouped by functionality. Each module should be self-contained with its own ports (interfaces) and adapters (implementations), following the ports and adapters architecture principles.
  - **/config:** Contains project related configurations that are common across all modules.
  - **/accounts:** Manages investor accounts creation and management.
  - **/transactions:** Handles creation, sending, and receiving of cryptocurrency transactions.
  - **/wallets:** Manages cryptocurrency addresses and wallet functionalities.
  - **/signing:** Responsible for the secure signing of transactions, potentially integrating with Hardware Security Modules (HSMs).
  - **/authentication:** Handles authentication mechanisms for users.
  - **/listener:** Listens to blockchain events and transactions.
  - **/confirmations:** Manages transaction confirmation processes.
  - **/core/shared:** Contains shared utilities and common functionalities like logging, error handling, and shared domain models. This is where cross-cutting concerns are addressed.

  - **/infrastructure:** Holds implementations of various infrastructure concerns like database access, external services integrations (e.g., blockchain APIs, HSM APIs), message brokers, and caching solutions. Infrastructure services are typically exposed to the modules via interfaces defined in the modules themselves, following the Dependency Inversion Principle.
- **/tests:** Tests


Each module in the /modules directory should follow the ports and adapters structure.

### My Stats:

[![commits](https://badgen.net/github/commits/mangekyousharingan/satoshi-guard/master)](https://github.com/mangekyousharingan/satoshi-guard/commits/master?icon=github&color=green)

## License

Satoshi-Guard is [MIT](https://choosealicense.com/licenses/mit/) licensed.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## Feedback

If you have any feedback, please reach out to me on: [![mangekyousharingan](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mangekyousharingan)
