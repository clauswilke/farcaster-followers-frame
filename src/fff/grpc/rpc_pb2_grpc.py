"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from . import hub_event_pb2 as hub__event__pb2
from . import message_pb2 as message__pb2
from . import onchain_event_pb2 as onchain__event__pb2
from . import request_response_pb2 as request__response__pb2
from . import username_proof_pb2 as username__proof__pb2

class HubServiceStub(object):
    """Note about http-api annotations:
    The `httpServer.ts` class implements a HTTP API wrapper on top of this gRPC API.
    The annotations below are used to verify that all the HTTP API endpoints are implemented.
    If you are adding a new RPC method, if there needs to be a corresponding HTTP API endpoint,
    add the annotation to the method. @http-api: none means that there is no corresponding HTTP API
    If there is no annotation, we assume there is a corresponding HTTP API endpoint with the same name as the RPC method
    Please see `httpServer.ts` for more details

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubmitMessage = channel.unary_unary('/HubService/SubmitMessage', request_serializer=message__pb2.Message.SerializeToString, response_deserializer=message__pb2.Message.FromString)
        self.ValidateMessage = channel.unary_unary('/HubService/ValidateMessage', request_serializer=message__pb2.Message.SerializeToString, response_deserializer=request__response__pb2.ValidationResponse.FromString)
        self.Subscribe = channel.unary_stream('/HubService/Subscribe', request_serializer=request__response__pb2.SubscribeRequest.SerializeToString, response_deserializer=hub__event__pb2.HubEvent.FromString)
        self.GetEvent = channel.unary_unary('/HubService/GetEvent', request_serializer=request__response__pb2.EventRequest.SerializeToString, response_deserializer=hub__event__pb2.HubEvent.FromString)
        self.GetCast = channel.unary_unary('/HubService/GetCast', request_serializer=message__pb2.CastId.SerializeToString, response_deserializer=message__pb2.Message.FromString)
        self.GetCastsByFid = channel.unary_unary('/HubService/GetCastsByFid', request_serializer=request__response__pb2.FidRequest.SerializeToString, response_deserializer=request__response__pb2.MessagesResponse.FromString)
        self.GetCastsByParent = channel.unary_unary('/HubService/GetCastsByParent', request_serializer=request__response__pb2.CastsByParentRequest.SerializeToString, response_deserializer=request__response__pb2.MessagesResponse.FromString)
        self.GetCastsByMention = channel.unary_unary('/HubService/GetCastsByMention', request_serializer=request__response__pb2.FidRequest.SerializeToString, response_deserializer=request__response__pb2.MessagesResponse.FromString)
        self.GetReaction = channel.unary_unary('/HubService/GetReaction', request_serializer=request__response__pb2.ReactionRequest.SerializeToString, response_deserializer=message__pb2.Message.FromString)
        self.GetReactionsByFid = channel.unary_unary('/HubService/GetReactionsByFid', request_serializer=request__response__pb2.ReactionsByFidRequest.SerializeToString, response_deserializer=request__response__pb2.MessagesResponse.FromString)
        self.GetReactionsByCast = channel.unary_unary('/HubService/GetReactionsByCast', request_serializer=request__response__pb2.ReactionsByTargetRequest.SerializeToString, response_deserializer=request__response__pb2.MessagesResponse.FromString)
        self.GetReactionsByTarget = channel.unary_unary('/HubService/GetReactionsByTarget', request_serializer=request__response__pb2.ReactionsByTargetRequest.SerializeToString, response_deserializer=request__response__pb2.MessagesResponse.FromString)
        self.GetUserData = channel.unary_unary('/HubService/GetUserData', request_serializer=request__response__pb2.UserDataRequest.SerializeToString, response_deserializer=message__pb2.Message.FromString)
        self.GetUserDataByFid = channel.unary_unary('/HubService/GetUserDataByFid', request_serializer=request__response__pb2.FidRequest.SerializeToString, response_deserializer=request__response__pb2.MessagesResponse.FromString)
        self.GetUsernameProof = channel.unary_unary('/HubService/GetUsernameProof', request_serializer=request__response__pb2.UsernameProofRequest.SerializeToString, response_deserializer=username__proof__pb2.UserNameProof.FromString)
        self.GetUserNameProofsByFid = channel.unary_unary('/HubService/GetUserNameProofsByFid', request_serializer=request__response__pb2.FidRequest.SerializeToString, response_deserializer=request__response__pb2.UsernameProofsResponse.FromString)
        self.GetVerification = channel.unary_unary('/HubService/GetVerification', request_serializer=request__response__pb2.VerificationRequest.SerializeToString, response_deserializer=message__pb2.Message.FromString)
        self.GetVerificationsByFid = channel.unary_unary('/HubService/GetVerificationsByFid', request_serializer=request__response__pb2.FidRequest.SerializeToString, response_deserializer=request__response__pb2.MessagesResponse.FromString)
        self.GetOnChainSigner = channel.unary_unary('/HubService/GetOnChainSigner', request_serializer=request__response__pb2.SignerRequest.SerializeToString, response_deserializer=onchain__event__pb2.OnChainEvent.FromString)
        self.GetOnChainSignersByFid = channel.unary_unary('/HubService/GetOnChainSignersByFid', request_serializer=request__response__pb2.FidRequest.SerializeToString, response_deserializer=request__response__pb2.OnChainEventResponse.FromString)
        self.GetOnChainEvents = channel.unary_unary('/HubService/GetOnChainEvents', request_serializer=request__response__pb2.OnChainEventRequest.SerializeToString, response_deserializer=request__response__pb2.OnChainEventResponse.FromString)
        self.GetIdRegistryOnChainEvent = channel.unary_unary('/HubService/GetIdRegistryOnChainEvent', request_serializer=request__response__pb2.FidRequest.SerializeToString, response_deserializer=onchain__event__pb2.OnChainEvent.FromString)
        self.GetIdRegistryOnChainEventByAddress = channel.unary_unary('/HubService/GetIdRegistryOnChainEventByAddress', request_serializer=request__response__pb2.IdRegistryEventByAddressRequest.SerializeToString, response_deserializer=onchain__event__pb2.OnChainEvent.FromString)
        self.GetCurrentStorageLimitsByFid = channel.unary_unary('/HubService/GetCurrentStorageLimitsByFid', request_serializer=request__response__pb2.FidRequest.SerializeToString, response_deserializer=request__response__pb2.StorageLimitsResponse.FromString)
        self.GetFids = channel.unary_unary('/HubService/GetFids', request_serializer=request__response__pb2.FidsRequest.SerializeToString, response_deserializer=request__response__pb2.FidsResponse.FromString)
        self.GetLink = channel.unary_unary('/HubService/GetLink', request_serializer=request__response__pb2.LinkRequest.SerializeToString, response_deserializer=message__pb2.Message.FromString)
        self.GetLinksByFid = channel.unary_unary('/HubService/GetLinksByFid', request_serializer=request__response__pb2.LinksByFidRequest.SerializeToString, response_deserializer=request__response__pb2.MessagesResponse.FromString)
        self.GetLinksByTarget = channel.unary_unary('/HubService/GetLinksByTarget', request_serializer=request__response__pb2.LinksByTargetRequest.SerializeToString, response_deserializer=request__response__pb2.MessagesResponse.FromString)
        self.GetAllCastMessagesByFid = channel.unary_unary('/HubService/GetAllCastMessagesByFid', request_serializer=request__response__pb2.FidRequest.SerializeToString, response_deserializer=request__response__pb2.MessagesResponse.FromString)
        self.GetAllReactionMessagesByFid = channel.unary_unary('/HubService/GetAllReactionMessagesByFid', request_serializer=request__response__pb2.FidRequest.SerializeToString, response_deserializer=request__response__pb2.MessagesResponse.FromString)
        self.GetAllVerificationMessagesByFid = channel.unary_unary('/HubService/GetAllVerificationMessagesByFid', request_serializer=request__response__pb2.FidRequest.SerializeToString, response_deserializer=request__response__pb2.MessagesResponse.FromString)
        self.GetAllUserDataMessagesByFid = channel.unary_unary('/HubService/GetAllUserDataMessagesByFid', request_serializer=request__response__pb2.FidRequest.SerializeToString, response_deserializer=request__response__pb2.MessagesResponse.FromString)
        self.GetAllLinkMessagesByFid = channel.unary_unary('/HubService/GetAllLinkMessagesByFid', request_serializer=request__response__pb2.FidRequest.SerializeToString, response_deserializer=request__response__pb2.MessagesResponse.FromString)
        self.GetInfo = channel.unary_unary('/HubService/GetInfo', request_serializer=request__response__pb2.HubInfoRequest.SerializeToString, response_deserializer=request__response__pb2.HubInfoResponse.FromString)
        self.GetSyncStatus = channel.unary_unary('/HubService/GetSyncStatus', request_serializer=request__response__pb2.SyncStatusRequest.SerializeToString, response_deserializer=request__response__pb2.SyncStatusResponse.FromString)
        self.GetAllSyncIdsByPrefix = channel.unary_unary('/HubService/GetAllSyncIdsByPrefix', request_serializer=request__response__pb2.TrieNodePrefix.SerializeToString, response_deserializer=request__response__pb2.SyncIds.FromString)
        self.GetAllMessagesBySyncIds = channel.unary_unary('/HubService/GetAllMessagesBySyncIds', request_serializer=request__response__pb2.SyncIds.SerializeToString, response_deserializer=request__response__pb2.MessagesResponse.FromString)
        self.GetSyncMetadataByPrefix = channel.unary_unary('/HubService/GetSyncMetadataByPrefix', request_serializer=request__response__pb2.TrieNodePrefix.SerializeToString, response_deserializer=request__response__pb2.TrieNodeMetadataResponse.FromString)
        self.GetSyncSnapshotByPrefix = channel.unary_unary('/HubService/GetSyncSnapshotByPrefix', request_serializer=request__response__pb2.TrieNodePrefix.SerializeToString, response_deserializer=request__response__pb2.TrieNodeSnapshotResponse.FromString)

class HubServiceServicer(object):
    """Note about http-api annotations:
    The `httpServer.ts` class implements a HTTP API wrapper on top of this gRPC API.
    The annotations below are used to verify that all the HTTP API endpoints are implemented.
    If you are adding a new RPC method, if there needs to be a corresponding HTTP API endpoint,
    add the annotation to the method. @http-api: none means that there is no corresponding HTTP API
    If there is no annotation, we assume there is a corresponding HTTP API endpoint with the same name as the RPC method
    Please see `httpServer.ts` for more details

    """

    def SubmitMessage(self, request, context):
        """Submit Methods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidateMessage(self, request, context):
        """Validation Methods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Event Methods
        @http-api: none
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEvent(self, request, context):
        """@http-api: events
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCast(self, request, context):
        """Casts
        @http-api: castById
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCastsByFid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCastsByParent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCastsByMention(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetReaction(self, request, context):
        """Reactions
        @http-api: reactionById
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetReactionsByFid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetReactionsByCast(self, request, context):
        """To be deprecated
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetReactionsByTarget(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserData(self, request, context):
        """User Data
        @http-api: none
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserDataByFid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsernameProof(self, request, context):
        """Username Proof
        @http-api: userNameProofByName
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserNameProofsByFid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVerification(self, request, context):
        """Verifications
        @http-api: none
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVerificationsByFid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOnChainSigner(self, request, context):
        """OnChain Events
        @http-api: none
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOnChainSignersByFid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOnChainEvents(self, request, context):
        """@http-api: none
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIdRegistryOnChainEvent(self, request, context):
        """@http-api: none
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIdRegistryOnChainEventByAddress(self, request, context):
        """@http-api: onChainIdRegistryEventByAddress
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCurrentStorageLimitsByFid(self, request, context):
        """@http-api: storageLimitsByFid
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFids(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLink(self, request, context):
        """Links
        @http-api: linkById
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLinksByFid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLinksByTarget(self, request, context):
        """@http-api: linksByTargetFid
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllCastMessagesByFid(self, request, context):
        """Bulk Methods
        The Bulk methods don't have corresponding HTTP API endpoints because the
        regular endpoints can be used to get all the messages
        @http-api: none
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllReactionMessagesByFid(self, request, context):
        """@http-api: none
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllVerificationMessagesByFid(self, request, context):
        """@http-api: none
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllUserDataMessagesByFid(self, request, context):
        """@http-api: none
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllLinkMessagesByFid(self, request, context):
        """@http-api: none
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInfo(self, request, context):
        """Sync Methods
        Outside the "info" RPC, the HTTP API doesn't implement any of the sync methods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSyncStatus(self, request, context):
        """@http-api: none
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllSyncIdsByPrefix(self, request, context):
        """@http-api: none
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllMessagesBySyncIds(self, request, context):
        """@http-api: none
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSyncMetadataByPrefix(self, request, context):
        """@http-api: none
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSyncSnapshotByPrefix(self, request, context):
        """@http-api: none
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_HubServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'SubmitMessage': grpc.unary_unary_rpc_method_handler(servicer.SubmitMessage, request_deserializer=message__pb2.Message.FromString, response_serializer=message__pb2.Message.SerializeToString), 'ValidateMessage': grpc.unary_unary_rpc_method_handler(servicer.ValidateMessage, request_deserializer=message__pb2.Message.FromString, response_serializer=request__response__pb2.ValidationResponse.SerializeToString), 'Subscribe': grpc.unary_stream_rpc_method_handler(servicer.Subscribe, request_deserializer=request__response__pb2.SubscribeRequest.FromString, response_serializer=hub__event__pb2.HubEvent.SerializeToString), 'GetEvent': grpc.unary_unary_rpc_method_handler(servicer.GetEvent, request_deserializer=request__response__pb2.EventRequest.FromString, response_serializer=hub__event__pb2.HubEvent.SerializeToString), 'GetCast': grpc.unary_unary_rpc_method_handler(servicer.GetCast, request_deserializer=message__pb2.CastId.FromString, response_serializer=message__pb2.Message.SerializeToString), 'GetCastsByFid': grpc.unary_unary_rpc_method_handler(servicer.GetCastsByFid, request_deserializer=request__response__pb2.FidRequest.FromString, response_serializer=request__response__pb2.MessagesResponse.SerializeToString), 'GetCastsByParent': grpc.unary_unary_rpc_method_handler(servicer.GetCastsByParent, request_deserializer=request__response__pb2.CastsByParentRequest.FromString, response_serializer=request__response__pb2.MessagesResponse.SerializeToString), 'GetCastsByMention': grpc.unary_unary_rpc_method_handler(servicer.GetCastsByMention, request_deserializer=request__response__pb2.FidRequest.FromString, response_serializer=request__response__pb2.MessagesResponse.SerializeToString), 'GetReaction': grpc.unary_unary_rpc_method_handler(servicer.GetReaction, request_deserializer=request__response__pb2.ReactionRequest.FromString, response_serializer=message__pb2.Message.SerializeToString), 'GetReactionsByFid': grpc.unary_unary_rpc_method_handler(servicer.GetReactionsByFid, request_deserializer=request__response__pb2.ReactionsByFidRequest.FromString, response_serializer=request__response__pb2.MessagesResponse.SerializeToString), 'GetReactionsByCast': grpc.unary_unary_rpc_method_handler(servicer.GetReactionsByCast, request_deserializer=request__response__pb2.ReactionsByTargetRequest.FromString, response_serializer=request__response__pb2.MessagesResponse.SerializeToString), 'GetReactionsByTarget': grpc.unary_unary_rpc_method_handler(servicer.GetReactionsByTarget, request_deserializer=request__response__pb2.ReactionsByTargetRequest.FromString, response_serializer=request__response__pb2.MessagesResponse.SerializeToString), 'GetUserData': grpc.unary_unary_rpc_method_handler(servicer.GetUserData, request_deserializer=request__response__pb2.UserDataRequest.FromString, response_serializer=message__pb2.Message.SerializeToString), 'GetUserDataByFid': grpc.unary_unary_rpc_method_handler(servicer.GetUserDataByFid, request_deserializer=request__response__pb2.FidRequest.FromString, response_serializer=request__response__pb2.MessagesResponse.SerializeToString), 'GetUsernameProof': grpc.unary_unary_rpc_method_handler(servicer.GetUsernameProof, request_deserializer=request__response__pb2.UsernameProofRequest.FromString, response_serializer=username__proof__pb2.UserNameProof.SerializeToString), 'GetUserNameProofsByFid': grpc.unary_unary_rpc_method_handler(servicer.GetUserNameProofsByFid, request_deserializer=request__response__pb2.FidRequest.FromString, response_serializer=request__response__pb2.UsernameProofsResponse.SerializeToString), 'GetVerification': grpc.unary_unary_rpc_method_handler(servicer.GetVerification, request_deserializer=request__response__pb2.VerificationRequest.FromString, response_serializer=message__pb2.Message.SerializeToString), 'GetVerificationsByFid': grpc.unary_unary_rpc_method_handler(servicer.GetVerificationsByFid, request_deserializer=request__response__pb2.FidRequest.FromString, response_serializer=request__response__pb2.MessagesResponse.SerializeToString), 'GetOnChainSigner': grpc.unary_unary_rpc_method_handler(servicer.GetOnChainSigner, request_deserializer=request__response__pb2.SignerRequest.FromString, response_serializer=onchain__event__pb2.OnChainEvent.SerializeToString), 'GetOnChainSignersByFid': grpc.unary_unary_rpc_method_handler(servicer.GetOnChainSignersByFid, request_deserializer=request__response__pb2.FidRequest.FromString, response_serializer=request__response__pb2.OnChainEventResponse.SerializeToString), 'GetOnChainEvents': grpc.unary_unary_rpc_method_handler(servicer.GetOnChainEvents, request_deserializer=request__response__pb2.OnChainEventRequest.FromString, response_serializer=request__response__pb2.OnChainEventResponse.SerializeToString), 'GetIdRegistryOnChainEvent': grpc.unary_unary_rpc_method_handler(servicer.GetIdRegistryOnChainEvent, request_deserializer=request__response__pb2.FidRequest.FromString, response_serializer=onchain__event__pb2.OnChainEvent.SerializeToString), 'GetIdRegistryOnChainEventByAddress': grpc.unary_unary_rpc_method_handler(servicer.GetIdRegistryOnChainEventByAddress, request_deserializer=request__response__pb2.IdRegistryEventByAddressRequest.FromString, response_serializer=onchain__event__pb2.OnChainEvent.SerializeToString), 'GetCurrentStorageLimitsByFid': grpc.unary_unary_rpc_method_handler(servicer.GetCurrentStorageLimitsByFid, request_deserializer=request__response__pb2.FidRequest.FromString, response_serializer=request__response__pb2.StorageLimitsResponse.SerializeToString), 'GetFids': grpc.unary_unary_rpc_method_handler(servicer.GetFids, request_deserializer=request__response__pb2.FidsRequest.FromString, response_serializer=request__response__pb2.FidsResponse.SerializeToString), 'GetLink': grpc.unary_unary_rpc_method_handler(servicer.GetLink, request_deserializer=request__response__pb2.LinkRequest.FromString, response_serializer=message__pb2.Message.SerializeToString), 'GetLinksByFid': grpc.unary_unary_rpc_method_handler(servicer.GetLinksByFid, request_deserializer=request__response__pb2.LinksByFidRequest.FromString, response_serializer=request__response__pb2.MessagesResponse.SerializeToString), 'GetLinksByTarget': grpc.unary_unary_rpc_method_handler(servicer.GetLinksByTarget, request_deserializer=request__response__pb2.LinksByTargetRequest.FromString, response_serializer=request__response__pb2.MessagesResponse.SerializeToString), 'GetAllCastMessagesByFid': grpc.unary_unary_rpc_method_handler(servicer.GetAllCastMessagesByFid, request_deserializer=request__response__pb2.FidRequest.FromString, response_serializer=request__response__pb2.MessagesResponse.SerializeToString), 'GetAllReactionMessagesByFid': grpc.unary_unary_rpc_method_handler(servicer.GetAllReactionMessagesByFid, request_deserializer=request__response__pb2.FidRequest.FromString, response_serializer=request__response__pb2.MessagesResponse.SerializeToString), 'GetAllVerificationMessagesByFid': grpc.unary_unary_rpc_method_handler(servicer.GetAllVerificationMessagesByFid, request_deserializer=request__response__pb2.FidRequest.FromString, response_serializer=request__response__pb2.MessagesResponse.SerializeToString), 'GetAllUserDataMessagesByFid': grpc.unary_unary_rpc_method_handler(servicer.GetAllUserDataMessagesByFid, request_deserializer=request__response__pb2.FidRequest.FromString, response_serializer=request__response__pb2.MessagesResponse.SerializeToString), 'GetAllLinkMessagesByFid': grpc.unary_unary_rpc_method_handler(servicer.GetAllLinkMessagesByFid, request_deserializer=request__response__pb2.FidRequest.FromString, response_serializer=request__response__pb2.MessagesResponse.SerializeToString), 'GetInfo': grpc.unary_unary_rpc_method_handler(servicer.GetInfo, request_deserializer=request__response__pb2.HubInfoRequest.FromString, response_serializer=request__response__pb2.HubInfoResponse.SerializeToString), 'GetSyncStatus': grpc.unary_unary_rpc_method_handler(servicer.GetSyncStatus, request_deserializer=request__response__pb2.SyncStatusRequest.FromString, response_serializer=request__response__pb2.SyncStatusResponse.SerializeToString), 'GetAllSyncIdsByPrefix': grpc.unary_unary_rpc_method_handler(servicer.GetAllSyncIdsByPrefix, request_deserializer=request__response__pb2.TrieNodePrefix.FromString, response_serializer=request__response__pb2.SyncIds.SerializeToString), 'GetAllMessagesBySyncIds': grpc.unary_unary_rpc_method_handler(servicer.GetAllMessagesBySyncIds, request_deserializer=request__response__pb2.SyncIds.FromString, response_serializer=request__response__pb2.MessagesResponse.SerializeToString), 'GetSyncMetadataByPrefix': grpc.unary_unary_rpc_method_handler(servicer.GetSyncMetadataByPrefix, request_deserializer=request__response__pb2.TrieNodePrefix.FromString, response_serializer=request__response__pb2.TrieNodeMetadataResponse.SerializeToString), 'GetSyncSnapshotByPrefix': grpc.unary_unary_rpc_method_handler(servicer.GetSyncSnapshotByPrefix, request_deserializer=request__response__pb2.TrieNodePrefix.FromString, response_serializer=request__response__pb2.TrieNodeSnapshotResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('HubService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class HubService(object):
    """Note about http-api annotations:
    The `httpServer.ts` class implements a HTTP API wrapper on top of this gRPC API.
    The annotations below are used to verify that all the HTTP API endpoints are implemented.
    If you are adding a new RPC method, if there needs to be a corresponding HTTP API endpoint,
    add the annotation to the method. @http-api: none means that there is no corresponding HTTP API
    If there is no annotation, we assume there is a corresponding HTTP API endpoint with the same name as the RPC method
    Please see `httpServer.ts` for more details

    """

    @staticmethod
    def SubmitMessage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/SubmitMessage', message__pb2.Message.SerializeToString, message__pb2.Message.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValidateMessage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/ValidateMessage', message__pb2.Message.SerializeToString, request__response__pb2.ValidationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_stream(request, target, '/HubService/Subscribe', request__response__pb2.SubscribeRequest.SerializeToString, hub__event__pb2.HubEvent.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEvent(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetEvent', request__response__pb2.EventRequest.SerializeToString, hub__event__pb2.HubEvent.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCast(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetCast', message__pb2.CastId.SerializeToString, message__pb2.Message.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCastsByFid(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetCastsByFid', request__response__pb2.FidRequest.SerializeToString, request__response__pb2.MessagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCastsByParent(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetCastsByParent', request__response__pb2.CastsByParentRequest.SerializeToString, request__response__pb2.MessagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCastsByMention(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetCastsByMention', request__response__pb2.FidRequest.SerializeToString, request__response__pb2.MessagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetReaction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetReaction', request__response__pb2.ReactionRequest.SerializeToString, message__pb2.Message.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetReactionsByFid(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetReactionsByFid', request__response__pb2.ReactionsByFidRequest.SerializeToString, request__response__pb2.MessagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetReactionsByCast(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetReactionsByCast', request__response__pb2.ReactionsByTargetRequest.SerializeToString, request__response__pb2.MessagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetReactionsByTarget(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetReactionsByTarget', request__response__pb2.ReactionsByTargetRequest.SerializeToString, request__response__pb2.MessagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserData(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetUserData', request__response__pb2.UserDataRequest.SerializeToString, message__pb2.Message.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserDataByFid(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetUserDataByFid', request__response__pb2.FidRequest.SerializeToString, request__response__pb2.MessagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUsernameProof(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetUsernameProof', request__response__pb2.UsernameProofRequest.SerializeToString, username__proof__pb2.UserNameProof.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserNameProofsByFid(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetUserNameProofsByFid', request__response__pb2.FidRequest.SerializeToString, request__response__pb2.UsernameProofsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVerification(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetVerification', request__response__pb2.VerificationRequest.SerializeToString, message__pb2.Message.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVerificationsByFid(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetVerificationsByFid', request__response__pb2.FidRequest.SerializeToString, request__response__pb2.MessagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOnChainSigner(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetOnChainSigner', request__response__pb2.SignerRequest.SerializeToString, onchain__event__pb2.OnChainEvent.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOnChainSignersByFid(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetOnChainSignersByFid', request__response__pb2.FidRequest.SerializeToString, request__response__pb2.OnChainEventResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOnChainEvents(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetOnChainEvents', request__response__pb2.OnChainEventRequest.SerializeToString, request__response__pb2.OnChainEventResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetIdRegistryOnChainEvent(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetIdRegistryOnChainEvent', request__response__pb2.FidRequest.SerializeToString, onchain__event__pb2.OnChainEvent.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetIdRegistryOnChainEventByAddress(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetIdRegistryOnChainEventByAddress', request__response__pb2.IdRegistryEventByAddressRequest.SerializeToString, onchain__event__pb2.OnChainEvent.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCurrentStorageLimitsByFid(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetCurrentStorageLimitsByFid', request__response__pb2.FidRequest.SerializeToString, request__response__pb2.StorageLimitsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFids(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetFids', request__response__pb2.FidsRequest.SerializeToString, request__response__pb2.FidsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLink(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetLink', request__response__pb2.LinkRequest.SerializeToString, message__pb2.Message.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLinksByFid(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetLinksByFid', request__response__pb2.LinksByFidRequest.SerializeToString, request__response__pb2.MessagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLinksByTarget(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetLinksByTarget', request__response__pb2.LinksByTargetRequest.SerializeToString, request__response__pb2.MessagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllCastMessagesByFid(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetAllCastMessagesByFid', request__response__pb2.FidRequest.SerializeToString, request__response__pb2.MessagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllReactionMessagesByFid(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetAllReactionMessagesByFid', request__response__pb2.FidRequest.SerializeToString, request__response__pb2.MessagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllVerificationMessagesByFid(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetAllVerificationMessagesByFid', request__response__pb2.FidRequest.SerializeToString, request__response__pb2.MessagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllUserDataMessagesByFid(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetAllUserDataMessagesByFid', request__response__pb2.FidRequest.SerializeToString, request__response__pb2.MessagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllLinkMessagesByFid(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetAllLinkMessagesByFid', request__response__pb2.FidRequest.SerializeToString, request__response__pb2.MessagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInfo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetInfo', request__response__pb2.HubInfoRequest.SerializeToString, request__response__pb2.HubInfoResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSyncStatus(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetSyncStatus', request__response__pb2.SyncStatusRequest.SerializeToString, request__response__pb2.SyncStatusResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllSyncIdsByPrefix(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetAllSyncIdsByPrefix', request__response__pb2.TrieNodePrefix.SerializeToString, request__response__pb2.SyncIds.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllMessagesBySyncIds(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetAllMessagesBySyncIds', request__response__pb2.SyncIds.SerializeToString, request__response__pb2.MessagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSyncMetadataByPrefix(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetSyncMetadataByPrefix', request__response__pb2.TrieNodePrefix.SerializeToString, request__response__pb2.TrieNodeMetadataResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSyncSnapshotByPrefix(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HubService/GetSyncSnapshotByPrefix', request__response__pb2.TrieNodePrefix.SerializeToString, request__response__pb2.TrieNodeSnapshotResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

class AdminServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RebuildSyncTrie = channel.unary_unary('/AdminService/RebuildSyncTrie', request_serializer=request__response__pb2.Empty.SerializeToString, response_deserializer=request__response__pb2.Empty.FromString)
        self.DeleteAllMessagesFromDb = channel.unary_unary('/AdminService/DeleteAllMessagesFromDb', request_serializer=request__response__pb2.Empty.SerializeToString, response_deserializer=request__response__pb2.Empty.FromString)
        self.SubmitOnChainEvent = channel.unary_unary('/AdminService/SubmitOnChainEvent', request_serializer=onchain__event__pb2.OnChainEvent.SerializeToString, response_deserializer=onchain__event__pb2.OnChainEvent.FromString)

class AdminServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RebuildSyncTrie(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAllMessagesFromDb(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitOnChainEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_AdminServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'RebuildSyncTrie': grpc.unary_unary_rpc_method_handler(servicer.RebuildSyncTrie, request_deserializer=request__response__pb2.Empty.FromString, response_serializer=request__response__pb2.Empty.SerializeToString), 'DeleteAllMessagesFromDb': grpc.unary_unary_rpc_method_handler(servicer.DeleteAllMessagesFromDb, request_deserializer=request__response__pb2.Empty.FromString, response_serializer=request__response__pb2.Empty.SerializeToString), 'SubmitOnChainEvent': grpc.unary_unary_rpc_method_handler(servicer.SubmitOnChainEvent, request_deserializer=onchain__event__pb2.OnChainEvent.FromString, response_serializer=onchain__event__pb2.OnChainEvent.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('AdminService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class AdminService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RebuildSyncTrie(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AdminService/RebuildSyncTrie', request__response__pb2.Empty.SerializeToString, request__response__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAllMessagesFromDb(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AdminService/DeleteAllMessagesFromDb', request__response__pb2.Empty.SerializeToString, request__response__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubmitOnChainEvent(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AdminService/SubmitOnChainEvent', onchain__event__pb2.OnChainEvent.SerializeToString, onchain__event__pb2.OnChainEvent.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)