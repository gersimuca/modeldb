package ai.verta.modeldb.common.config;

public class NFSConfig {
  private String nfsUrlProtocol = "https";
  private String nfsRootPath;
  private String nfsServerHost = "";
  private NFSEndpointConfig artifactEndpoint;
  private String nfsPathPrefix;

  public void Validate(String base) throws InvalidConfigException {
    if (nfsRootPath == null || nfsRootPath.isEmpty())
      throw new InvalidConfigException(base + ".nfsRootPath", Config.MISSING_REQUIRED);

    if (artifactEndpoint == null)
      throw new InvalidConfigException(base + ".artifactEndpoint", Config.MISSING_REQUIRED);
    artifactEndpoint.Validate(base + ".artifactEndpoint");
  }

  public String storeTypePathPrefix() {
    var pathPrefix = String.format("nfs://%s/", nfsRootPath);
    if (nfsPathPrefix != null && !nfsPathPrefix.isEmpty()) {
      pathPrefix += nfsPathPrefix + "/";
    }
    return pathPrefix;
  }

  public String getNfsRootPath() {
    return nfsRootPath;
  }

  public NFSEndpointConfig getArtifactEndpoint() {
    return artifactEndpoint;
  }
}
