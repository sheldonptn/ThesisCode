import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:pat.root'
    )
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('fit_tf.root')
                                   )


process.demo = cms.EDAnalyzer('FitBTag_TF',
                              s_bdisc_name = cms.string('combinedSecondaryVertexBJetTags')
                              )


process.p = cms.Path(process.demo)
