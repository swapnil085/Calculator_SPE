node {
    def app
    /*Taking the Jenkinsfile from the git repository*/
    stage('Clone repository') {
        checkout scm
    }

    /*pytest for testing calculator*/       
    stage('Run pytest') {
        sh 'pip install pytest'
        sh 'python -m pytest'
    }

    
    /* Building the image */
    stage('Build image') {
        app = docker.build("rishi12398/python_calculator")
    }
    /*Pushing the new image to dockerhub with tag: latest*/
    stage('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', '1b9136eb-616a-46c7-a024-e3caea811fd9') {
            app.push("latest")
            } 
                echo "Trying to Push Docker Build to DockerHub"
    }
    /*Deploy Image using Rundeck*/
    stage('Deploy') {
        build 'Rundeck_Deploy_Calculator'
    }
}