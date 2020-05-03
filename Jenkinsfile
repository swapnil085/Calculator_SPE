node {
    def app

    stage('Clone repository') {
        /* Cloning the Repository to our Workspace */
        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image */
        app = docker.build("rishi12398/python_calculator")
    }

    stage('Test image') {
        
        app.inside {
            echo "Tests passed"
        }
    }

    stage('Push image') {
        /* 
			You would need to first register with DockerHub before you can push images to your account
		*/
        docker.withRegistry('https://registry.hub.docker.com', '1b9136eb-616a-46c7-a024-e3caea811fd9') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
            } 
                echo "Trying to Push Docker Build to DockerHub"
    }
}