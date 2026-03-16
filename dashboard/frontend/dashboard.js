function updateClusterStatus() {
    document.getElementById("cluster").innerText =
        "Cluster healthy - CPU utilization 42%";
}

function showAlert() {
    document.getElementById("alerts").innerText =
        "AI detected abnormal latency in payment-service";
}

function showAutomation() {
    document.getElementById("actions").innerText =
        "Operator scaled payment-service from 2 pods to 3 pods";
}

setTimeout(updateClusterStatus, 2000);
setTimeout(showAlert, 5000);
setTimeout(showAutomation, 8000);
