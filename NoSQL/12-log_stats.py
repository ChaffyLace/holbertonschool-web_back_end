#!/usr/bin/env python3
"""
Fournit des statistiques sur les journaux Nginx stockés dans MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """
    Affiche le nombre total de logs, le nombre par méthode
    et le nombre de vérifications de statut.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Nombre total de documents
    # Note: count_documents({}) est préférable à estimated_document_count()
    # pour une précision totale lors des tests
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Vérification spécifique du chemin /status
    status_check = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()