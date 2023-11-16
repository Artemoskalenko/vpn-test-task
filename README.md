# Installation

- Cloning the repository

    `git clone https://github.com/Artemoskalenko/vpn-test-task.git`


- Running a docker container:
    ```
    cd vpn-test-task
    docker-compose build
    docker-compose up
    ```

- Browse `127.0.0.1:8000` or `localhost:8000`

After raising the Docker container, the database will be created automatically, migrations will be applied and the admin user will be created.
- Login: admin
- Password: admin



# Endpoints

## User

- Login page:
  - **HTTP Method:** GET/POST
  - **URL:** `/login/`
  - **Description:** Displays the login page where the user can log into the account.

- Register page:
  - **HTTP Method:** GET/POST
  - **URL:** `/register/`
  - **Description:** Displays the registration page where the user can register a new account.

- Logout:
  - **HTTP Method:** GET
  - **URL:** `/logout/`
  - **Description:** Allows the user to log out of the account and go to the login page.

- Profile page:
  - **HTTP Method:** GET/POST
  - **URL:** `/profile/`
  - **Description:** Displays the user page where the user can see account information and change some user information.

## Site

- Sites page:
  - **HTTP Method:** GET/POST
  - **URL:** `/sites/`
  - **Description:** Displays a page with sites available to the user and a form for adding a new site.
    
- Delete a site:
  - **HTTP Method:** GET
  - **URL:** `/sites/delete/{site_id}/`
  - **Description:** Deletes a site by site ID.

- Statistics page:
  - **HTTP Method:** GET
  - **URL:** `/statistics/`
  - **Description:** Displays a page with statistics of sites available to the user.

- Website page via VPN:
  - **HTTP Method:** GET/POST
  - **URL:** `/{site_name}/`
  - **Description:** Going to the site via VPN.

- Website page via VPN (with additional path):
  - **HTTP Method:** GET/POST
  - **URL:** `/{site_name}/{site_path}/`
  - **Description:** Going deeper into the site via VPN.