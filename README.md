# LEO-Network-Visualizer

Due to being outdated, the visualization features of the [Hypatia Network Simulator](https://github.com/snkas/hypatia) are currently almost unusable. This project updates Hypatia's visualization capabilities.



## Visualize Constellations

You can follow the steps below to visualize your custom constellations:

1. **Set up the environment:** Create a Python environment (version >= 3.8) and run `pip install -r requirements.txt` to install the necessary dependencies.

2. **Configure Cesium Token:** Obtain your own Token from Cesium and paste it into the `Cesium.Ion.defaultAccessToken` field located in `./static_html/top.html`.

3. **Customize parameters:** Define your custom constellation parameters in `visualize_constellation.py`.

4. **Generate the visualization:** Run `visualize_constellation.py`. This will generate the corresponding HTML file in the `./CesiumApp` directory.

5. **Start the server:** Install **Node.js** and **http-server**. Then, navigate to the application directory and start the server:

   Bash

   ```
   cd ./CesiumAPP
   http-server -p 8081
   ```

6. **View results:** Open your web browser and navigate to `http://127.0.0.1:8081/<constellation.html>`, replacing `<constellation.html>` with the name of the generated HTML visualization file.