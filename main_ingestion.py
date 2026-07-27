from src.ingestion.cargador_documentos import CargadorDocumentos
from src.ingestion.divisor_documentos import DivisorDocumentos
from src.embeddings.vectorstore import VectorStore


print("=" * 60)
print("Santos Pegasus Soluciones")
print("Proceso de Ingestión")
print("=" * 60)

documentos = CargadorDocumentos().cargar()
chunks = DivisorDocumentos().dividir(documentos)

print(f"\nChunks generados: {len(chunks)}")
VectorStore().crear(chunks)
print("\nProceso finalizado.")