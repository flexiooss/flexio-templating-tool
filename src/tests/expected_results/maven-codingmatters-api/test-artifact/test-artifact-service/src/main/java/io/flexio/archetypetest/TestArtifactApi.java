package io.flexio.archetypetest;

import io.flexio.services.support.api.Api;
import org.codingmatters.rest.api.Processor;
import com.fasterxml.jackson.core.JsonFactory;
import io.flexio.archetypetest.api.TestArtifactDescriptor;
import io.flexio.archetypetest.api.TestArtifactHandlers;
import io.flexio.archetypetest.service.TestArtifactProcessor;

public class TestArtifactApi implements Api {

    private TestArtifactHandlers handlers;
    private TestArtifactProcessor processor;

    public TestArtifactApi(){
        this.handlers = new TestArtifactHandlers.Builder()
                            .build();

        this.processor = new TestArtifactProcessor(this.path(), new JsonFactory(), handlers);
    }

    @Override
    public Processor processor() {
        return this.processor;
    }

    @Override
    public String docResource() {
        return "test-artifact.html";
    }

    @Override
    public String name() {
        return TestArtifactDescriptor.NAME;
    }

    @Override
    public String version() {
        return "v2";
    }
}

