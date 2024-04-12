# song-recomendation-django
Hometown Beats: Personalized Song Recommendations

Hometown Beats is an innovative music recommendation platform that leverages user's hometowns to curate personalized playlists. Powered by .NET Core, Spotify API integration, and a microservices architecture, this project offers a seamless and tailored music experience.

Key Features:

1 - Personalized Recommendations: By analyzing user's hometown data, the system generates playlists tailored to their geographical preferences.

2 - Spotify Integration: Utilizing the Spotify API, users have access to a vast library of songs to enjoy based on their hometown.

3 - Microservices Architecture: The project is built on a microservices architecture, featuring separate services for the API gateway, weather service, and user service, enhancing scalability and maintainability.

4 - Docker Compose: With Docker Compose, the entire application, including microservices and the SQL Server database, can be easily deployed and managed in a containerized environment.


How it Works:

* The user's hometown data is collected and processed by the user service microservice.

* The weather service microservice retrieves weather data for the user's location to further refine song recommendations.

* The API gateway microservice interacts with the Spotify API to fetch song recommendations based on the user's hometown and weather conditions.

* Users can access personalized playlists via the Hometown Beats web or mobile interface.

Benefits:

Personalization: Users receive curated playlists that resonate with their hometown experiences and current weather conditions.
Scalability: The microservices architecture ensures the system can handle a growing user base and evolving features.
Ease of Deployment: Docker Compose simplifies the deployment process, enabling seamless setup and management of the entire application stack.
Hometown Beats offers a unique music discovery experience, blending the familiarity of hometown vibes with the excitement of discovering new tracks, all within a modern and scalable architecture.


